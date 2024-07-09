import io
import json
import logging
import pickle
import joblib

import pandas as pd
import tensorflow as tf
import xarray as xr
import pyarrow.parquet as pq

from app.celery_worker import celery_app
from app.utils.grace_helpers import load_scaler, get_time_dict

logger = logging.getLogger(__name__)


@celery_app.task
def predict_grace(file_content: bytes) -> dict:
    logger.info("Starting GRACE prediction")
    scaler = load_scaler()
    # Load the GRACE model
    grace_model = tf.keras.models.load_model("/code/model_files/ms_cnn_model/")
    scaler = joblib.load("/code/model_files/scaler.save")
    try:
        # Create a BytesIO object from the file content
        file_obj = io.BytesIO(file_content)

        # Read the parquet file
        table = pq.read_table(file_obj)
        ts_df = table.to_pandas()[
            [
                "lat",
                "lon",
                "time",
                "aet",
                "def",
                "pdsi",
                "pet",
                "pr",
                "srad",
                "ro",
                "soil",
                "swe",
                "precip",
            ]
        ]

        logger.info(f"Parquet file read successfully. Shape: {ts_df.shape}")

        if len(ts_df.dropna()) > 0:
            # Prepare input for the model
            time_dict = get_time_dict()
            ts_df["time"] = ts_df.time.dt.strftime("%Y-%m-%d").map(time_dict)
            ts_df = ts_df.dropna()
            ts_test_x = ts_df.to_numpy()
            ts_step_scaled = scaler.transform(ts_test_x)
            ts_pred = grace_model.predict(ts_step_scaled)

            # Create output DataFrame
            output_df = pd.DataFrame(ts_pred, columns=["lwe_thickness"])
            final_ts_df = pd.concat([ts_df[["lat", "lon", "time"]], output_df], axis=1)
            final_ts_df["time"] = final_ts_df["time"].map(
                dict(zip(time_dict.values(), time_dict.keys()))
            )
            final_ts_df["time"] = pd.to_datetime(final_ts_df.time)
            ds = final_ts_df.groupby(["lat", "lon", "time"]).mean().to_xarray()

            logger.info("GRACE prediction completed successfully")
            return ds.to_dict()
        else:
            raise ValueError("Input data is empty or contains only NaN values")
    except Exception as e:
        logger.error(f"Error in GRACE prediction: {str(e)}")
        raise

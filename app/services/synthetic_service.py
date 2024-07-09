import io
import json
import logging
import random
import tempfile
import zipfile
import os

import geopandas as gpd
import pandas as pd
from sdv.sequential import PARSynthesizer
from shapely.geometry import Point

from app.celery_worker import celery_app
from app.utils import CustomJSONEncoder

logger = logging.getLogger(__name__)


@celery_app.task
def generate_synthetic_data(num_wells: int, shapefile_content: bytes) -> dict:
    logger.info(f"Starting synthetic data generation for {num_wells} wells")

    # Load the synthetic data model
    model = PARSynthesizer.load("/code/model_files/synthetic.pkl")

    try:
        # Create a temporary directory to extract the zip file
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, "shapefile.zip")
            with open(zip_path, "wb") as zip_file:
                zip_file.write(shapefile_content)

            # Extract the zip file
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)

            # Find the .shp file
            shp_files = [f for f in os.listdir(tmpdir) if f.endswith(".shp")]
            if not shp_files:
                raise ValueError("No .shp file found in the uploaded zip file")
            shp_file = shp_files[0]
            shp_path = os.path.join(tmpdir, shp_file)

            # Read the shapefile
            gdf = gpd.read_file(shp_path)

        logger.info(f"Shapefile read successfully. Shape: {gdf.shape}")

        all_points = []
        for _, row in gdf.iterrows():
            all_points.extend(random_points_in_polygon(num_wells, row["geometry"]))

        while len(all_points) > num_wells:
            all_points.pop()

        logger.info(f"Generated {len(all_points)} random points")

        synthetic_data = model.sample(num_wells)

        logger.info(f"Generated synthetic data for {num_wells} wells")

        point_data = pd.DataFrame(
            {
                "Well_UUID": synthetic_data["Well_UUID"].unique().tolist(),
                "geometry": all_points,
            }
        )
        geosynth_data = pd.merge(
            synthetic_data, point_data, on="Well_UUID", how="inner"
        )
        geosynth_data = gpd.GeoDataFrame(geosynth_data, geometry="geometry")
        geosynth_data = geosynth_data.sort_values(by=["Well_UUID", "Date"])

        logger.info("Synthetic data generation completed successfully")
        result = json.loads(geosynth_data.to_json(cls=CustomJSONEncoder))
        return result
    except Exception as e:
        logger.error(f"Error in synthetic data generation: {str(e)}")
        raise


def random_points_in_polygon(number, polygon):
    points = []
    min_x, min_y, max_x, max_y = polygon.bounds
    while len(points) < number:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
        )
        if random_point.within(polygon):
            points.append(random_point)
    return points


@celery_app.task
def add(x, y):
    return x + y

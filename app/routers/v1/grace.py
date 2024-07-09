import io

import pyarrow.parquet as pq
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.models.grace_model import GRACEOutput
from app.services.grace_service import predict_grace
from app.utils.auth import verify_api_key

router = APIRouter()


@router.post("/grace/predict", response_model=dict)
async def grace_predict(
    file: UploadFile = File(...), api_key: str = Depends(verify_api_key)
):
    try:
        contents = await file.read()
        # Try to read the file as a parquet file
        try:
            pq.ParquetFile(io.BytesIO(contents))
        except Exception:
            raise HTTPException(
                status_code=400, detail="File must be a valid parquet file"
            )

        task = predict_grace.delay(contents)
        return {"task_id": str(task.id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/grace/result/{task_id}", response_model=GRACEOutput)
async def get_grace_result(task_id: str, api_key: str = Depends(verify_api_key)):
    task = predict_grace.AsyncResult(task_id)
    if task.state == "PENDING":
        return GRACEOutput(status="pending")
    elif task.state == "SUCCESS":
        return GRACEOutput(status="success", result=task.result)
    else:
        return GRACEOutput(status="failed", error=str(task.result))

from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from app.models.synthetic_model import SyntheticInput, SyntheticOutput
from app.services.synthetic_service import generate_synthetic_data
from app.utils.auth import verify_api_key

router = APIRouter()

@router.post("/synthetic/generate", response_model=dict)
async def synthetic_generate(
    num_wells: int = Form(...),
    shapefile: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    contents = await shapefile.read()
    task = generate_synthetic_data.delay(num_wells, contents)
    return {"task_id": str(task.id)}

@router.get("/synthetic/result/{task_id}", response_model=SyntheticOutput)
async def get_synthetic_result(task_id: str, api_key: str = Depends(verify_api_key)):
    task = generate_synthetic_data.AsyncResult(task_id)
    if task.state == 'PENDING':
        return SyntheticOutput(status='pending')
    elif task.state == 'SUCCESS':
        return SyntheticOutput(status='success', result=task.result)
    else:
        return SyntheticOutput(status='failed')
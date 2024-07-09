from fastapi import FastAPI
from app.routers.v1 import grace, synthetic

app = FastAPI(title="GRACE and Synthetic Well Data API")

app.include_router(grace.router, prefix="/api/v1")
app.include_router(synthetic.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the GRACE and Synthetic Well Data API"}
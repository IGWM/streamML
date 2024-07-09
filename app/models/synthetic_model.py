from pydantic import BaseModel
from typing import Optional, Any

class SyntheticInput(BaseModel):
    num_wells: int

class SyntheticOutput(BaseModel):
    status: str
    result: Optional[Any] = None
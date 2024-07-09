from pydantic import BaseModel
from typing import Optional, Any

class GRACEOutput(BaseModel):
    status: str
    result: Optional[Any] = None
    error: Optional[str] = None
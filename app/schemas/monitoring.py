from typing import List
from pydantic import BaseModel

class SystemStatus(BaseModel):
    name: str
    status: str

class StatusSummary(BaseModel):
    systems: List[SystemStatus]
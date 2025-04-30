from typing import List
from pydantic import BaseModel

class SystemStatus(BaseModel):
    name: str
    status: str

class StatusSummary(BaseModel):
    systems: List[SystemStatus]

class SystemsUptimes(BaseModel):
    name: str
    uptime: int

class Uptimes(BaseModel):
    uptimes: List[SystemsUptimes]

class Alerts(BaseModel):
    alerts: List[str]
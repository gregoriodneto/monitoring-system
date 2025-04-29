from fastapi import FastAPI
from app.routers.monitoring import router as monitoring_router

app = FastAPI()

app.include_router(monitoring_router, prefix="/api")
import os
import random
from fastapi import FastAPI
from dotenv import load_dotenv

if os.getenv("ENV") is None:
    load_dotenv()

ENV = os.getenv("ENV", "development")

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return { "status": "ok", "env": ENV }

@app.get("/metrics")
def metricks():
    return { "cpu_usage": f"{random.randint(10,90)}%", "memory_usage": f"{random.randint(100,800)}MB" }
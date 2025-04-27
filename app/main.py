import os
from fastapi import FastAPI
from dotenv import load_dotenv

if os.getenv("ENV") is None:
    load_dotenv()

ENV = os.getenv("ENV", "development")

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return { "status": "ok", "env": ENV }
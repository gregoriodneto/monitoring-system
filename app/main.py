import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV")

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    if ENV == "staging":
        return { "status": "Running in staging environment" }
    return { "status": "ok" }
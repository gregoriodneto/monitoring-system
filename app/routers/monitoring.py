import os
import random
from fastapi import APIRouter
from dotenv import load_dotenv
from app.schemas.monitoring import StatusSummary, Uptimes, Alerts

if os.getenv("ENV") is None:
    load_dotenv()

ENV                     = os.getenv("ENV", "development")
AUTHOR_SYSTEM           = os.getenv("AUTHOR_SYSTEM", "none")
VERSION_SYSTEM          = os.getenv("VERSION_SYSTEM", "none")
DESCRIPTION_SYSTEM      = os.getenv("DESCRIPTION_SYSTEM", "none")
NAME_SYSTEM             = os.getenv("NAME_SYSTEM", "none")

router = APIRouter()

@router.get("/healthcheck")
def healthcheck():
    return { "status": "ok", "env": ENV }

@router.get("/metrics")
def metricks():
    return { "cpu_usage": f"{random.randint(10,90)}%", "memory_usage": f"{random.randint(100,800)}MB" }

@router.get("/info")
def info():
    return {
        "name": NAME_SYSTEM,
        "version": VERSION_SYSTEM,
        "description": DESCRIPTION_SYSTEM,
        "author": AUTHOR_SYSTEM,
        "environment": ENV
    }

@router.post("/status-summary")
async def status_summary(status: StatusSummary):
    total = len(status.systems)
    ok_count = sum(1 for s in status.systems if s.status.lower() == "ok")
    fail_count = total - ok_count
    percent_ok = round((ok_count / total) * 100, 1) if total else 0.0
    return {
        "total": total,
        "ok": ok_count,
        "fail": fail_count,
        "percent_ok": percent_ok
    }

@router.post("/uptime-rank")
async def uptime_rank(uptime: Uptimes):
    classificacao = sorted(uptime.uptimes, key=lambda system: system.uptime, reverse=True)    
    return classificacao

@router.post("/alert-count")
async def alert_count(alert: Alerts):
    alert_counts = {}
    for alert in alert.alerts:
        if alert not in alert_counts:
            alert_counts[alert] = 0
        alert_counts[alert] += 1
    
    return alert_counts
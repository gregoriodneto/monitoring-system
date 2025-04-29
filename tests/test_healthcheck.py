import sys
import os
from fastapi.testclient import TestClient
from app.main import app

sys.path.insert(0, '/app')

client = TestClient(app)

def test_healthcheck():
    response = client.get("/api/healthcheck")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "env" in data

def test_metrics():
    response = client.get("/api/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "cpu_usage" in data
    assert "memory_usage" in data

def test_info():
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "description" in data
    assert "author" in data
    assert "environment" in data
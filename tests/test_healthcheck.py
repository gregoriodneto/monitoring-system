import sys
import os
from fastapi.testclient import TestClient
from app.main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "env" in data
from fastapi.testclient import TestClient
from app.main import app
def test_health_endpoint():
    r=TestClient(app).get("/api/health")
    assert r.status_code==200
    assert r.json()["status"]=="ok"

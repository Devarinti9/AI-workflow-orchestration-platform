from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_records_endpoint_exists():
    response = client.get("/records")
    assert response.status_code == 200
    assert "records" in response.json()

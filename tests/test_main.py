from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sum_valid():
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_sum_invalid():
    response = client.get("/sum?a=abc&b=3")
    assert response.status_code == 422  # FastAPI handles validation automatically


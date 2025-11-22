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

def test_product_valid():
    response = client.get("/product?a=4&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}

def test_product_invalid():
    response = client.get("/product?a=4&b=xyz")
    assert response.status_code == 422  # FastAPI handles validation automatically

# def test_divide_valid():
#     response = client.get("/divide?a=10&b=2")
#     assert response.status_code == 200
#     assert response.json() == {"result": 5}

# def test_divide_by_zero():
#     response = client.get("/divide?a=10&b=0")
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Division by zero is not allowed"}   

# def test_divide_invalid():
#     response = client.get("/divide?a=10&b=abc")
#     assert response.status_code == 422  # FastAPI handles validation automatically    
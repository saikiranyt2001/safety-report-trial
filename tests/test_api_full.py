from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Safety Platform Running"}

def test_reports():
    response = client.get("/api/reports")
    assert response.status_code in [200, 404]  # Adjust as needed

def test_analytics():
    response = client.get("/api/analytics")
    assert response.status_code in [200, 404]

def test_admin():
    response = client.get("/api/admin")
    assert response.status_code in [200, 404]

def test_uploads():
    response = client.get("/api/uploads")
    assert response.status_code in [200, 404]

def test_validation():
    response = client.get("/api/validation")
    assert response.status_code in [200, 404]

def test_auth():
    response = client.get("/api/auth")
    assert response.status_code in [200, 404]

# Add more tests for POST, PUT, DELETE endpoints as needed

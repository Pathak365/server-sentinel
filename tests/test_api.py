
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "Server Sentinel"


def test_system_endpoint():
    response = client.get("/api/v1/system")

    assert response.status_code == 200

    data = response.json()

    assert "cpu_uses" in data
    assert "memory_uses" in data
    assert "disk_uses" in data
    assert "host_name" in data
    assert "ip_address" in data


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["health_status"] in ["Healthy", "Unhealthy"]
    assert "timestamp" in data
    assert "failed_checks" in data


def test_history_endpoint():
    response = client.get("/api/v1/history")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_missing_history_record():
    response = client.get("/api/v1/history/nonexistent-record")

    assert response.status_code == 404

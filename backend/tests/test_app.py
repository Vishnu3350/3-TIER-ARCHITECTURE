import pytest

from backend.app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)

    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "claims-backend",
        "status": "healthy",
    }


def test_create_claim_requires_customer_and_amount(client):
    response = client.post(
        "/api/claims",
        json={"description": "Missing required information"},
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Customer name and amount are required"
    }


def test_update_claim_rejects_invalid_status(client):
    response = client.put(
        "/api/claims/1",
        json={"status": "Unknown"},
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Invalid status"
    }
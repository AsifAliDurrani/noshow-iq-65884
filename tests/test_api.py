from fastapi.testclient import TestClient
from noshow_iq.api import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200


def test_predict_endpoint():
    sample_payload = {
        "age": 30,
        "gender": "M",
        "appointment_day": "Wednesday",
        "sms_received": 1,
    }

    response = client.post("/predict", json=sample_payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

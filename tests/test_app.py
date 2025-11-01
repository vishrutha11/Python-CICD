from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    # nosec is used to ignore Bandit warning about asserts
    assert response.status_code == 200  # nosec
    expected = {"message": "Hello from FastAPI app deployed on GKE!"}
    assert response.json() == expected  # nosec

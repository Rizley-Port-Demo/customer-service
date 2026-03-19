import pytest
from app import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
def test_health(client):
    res = client.get("/health")
    assert res.json["status"] == "ok"

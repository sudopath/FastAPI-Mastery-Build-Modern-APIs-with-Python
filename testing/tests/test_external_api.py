import pytest
from fastapi.testclient import TestClient
from app.main import app
import httpx

client = TestClient(app)

@pytest.fixture
def mock_external_api(mocker):
    mock_response = {
        "userId": 1,
        "id": 1,
        "title": "Test todo",
        "completed": False
        }
    mocker.patch('httpx.AsyncClient.get', return_value=mocker.Mock(json=lambda: mock_response))

def test_fetch_external_data(mock_external_api):
    response = client.get('/external-data')
    assert response.status_code == 200
    assert response.json()["title"] == "Test todo"

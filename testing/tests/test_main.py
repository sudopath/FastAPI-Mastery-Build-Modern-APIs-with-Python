from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI"}

def test_create_item():
    response = client.post("/items/", params={"name": "Test Item", "description": "This is a test item"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_read_item():
    create_response = client.post("/items/", params={"name": "Test Item", "description": "This is a test item"})   
    item_id = create_response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id

def test_read_non_existent_item():
    response = client.get("/items/12345")
    assert response.status_code == 404
    assert response.json() == {"detail":"Item not found"}
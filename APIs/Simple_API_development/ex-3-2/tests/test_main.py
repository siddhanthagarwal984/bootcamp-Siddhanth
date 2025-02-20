from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/1", json={
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1500.00,
        "quantity": 5
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Item added"

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_update_item():
    response = client.put("/items/1", json={
        "name": "Updated Laptop",
        "description": "Updated Gaming laptop",
        "price": 1800.00,
        "quantity": 3
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Item updated"

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"

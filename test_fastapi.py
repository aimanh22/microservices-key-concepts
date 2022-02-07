from fastapi import FastAPI
from fastapi.testclient import TestClient
from mainFastApi import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

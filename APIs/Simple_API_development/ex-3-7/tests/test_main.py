from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_file():
    """Test uploading a file to the server."""
    file_content = b"Hello, this is a test file!"
    
    response = client.post(
        "/upload/",
        files={"file": ("test.txt", file_content, "text/plain")}
    )
    
    assert response.status_code == 200
    assert response.json()["filename"] == "test.txt"
    assert response.json()["message"] == "File uploaded successfully"

# FastAPI File Upload Example (ex-3-7)

## 📌 Overview
This API allows users to upload files and stores them in the `uploads/` directory.

## 🚀 How to Run

1. Install dependencies:
poetry install

2. Run the FastAPI server:

poetry run uvicorn app.main:app --reload

3. Open API docs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



## How to Test the API
1️⃣ Using Curl

curl -X 'POST' 'http://127.0.0.1:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test.txt'


2️⃣ Using Python Requests

import requests

url = "http://127.0.0.1:8000/upload/"
file_path = "test.txt"

with open(file_path, "rb") as file:
    files = {"file": (file_path, file, "text/plain")}
    response = requests.post(url, files=files)
    print(response.json())


3️⃣ Running Automated Tests

poetry run pytest



# FastAPI Static Files Example (ex-3-8)

## 📌 Overview
This API serves static files (e.g., images, HTML, CSS) using FastAPI.

## 🚀 How to Run

1. Install dependencies:
poetry install

2. Run the FastAPI server:
poetry run uvicorn app.main:app --reload


3. Open API docs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## 🛠️ How to Access Static Files
Once the server is running, open a web browser and visit:

http://127.0.0.1:8000/static/example.jpg


Any files inside the `static/` folder will be **accessible via the `/static/` route**.



## To Run the API

Start the FastAPI server:

poetry run uvicorn app.main:app --reload

Open your browser and visit:
http://127.0.0.1:8000/static/example.jpg

You should see the example.jpg file being displayed.

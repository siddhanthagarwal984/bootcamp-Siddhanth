## Run the Server:

poetry run uvicorn app.main:app --reload




## Test URLs:

http://127.0.0.1:8000/items/5 → {"item_id": 5}
http://127.0.0.1:8000/items/5?q=hello → {"item_id": 5, "query": "hello"}
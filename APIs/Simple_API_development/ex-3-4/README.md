## Run the Server

poetry run uvicorn app.main:app --reload

## Test with JSON:

Send this JSON to http://127.0.0.1:8000/items/:

{
    "name": "Laptop",
    "description": "Gaming Laptop",
    "price": 1500.0,
    "quantity": 5
}


## Using Postman (Graphical Interface)

1. Open Postman (download if not installed: https://www.postman.com/).
2. Select POST request.
3. Enter URL: http://127.0.0.1:8000/items/
4. Go to the Body tab and select raw.
5. Choose JSON as the format.
6. Enter the JSON payload:

{
    "name": "Laptop",
    "description": "Gaming Laptop",
    "price": 1500.0,
    "quantity": 5
}

7. Click Send.


## Response:

{
    "message": "Item created",
    "item": {
        "name": "Laptop",
        "description": "Gaming Laptop",
        "price": 1500.0,
        "quantity": 5
    }
}
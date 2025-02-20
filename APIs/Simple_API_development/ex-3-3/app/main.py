from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "query": q}
    return {"item_id": item_id}

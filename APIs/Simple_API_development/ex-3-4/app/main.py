from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}

from fastapi import FastAPI, HTTPException
from app.database import database, engine, metadata
from app.models import items
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/items/")
async def create_item(item: Item):
    query = items.insert().values(
        name=item.name, description=item.description, price=item.price, quantity=item.quantity
    )
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

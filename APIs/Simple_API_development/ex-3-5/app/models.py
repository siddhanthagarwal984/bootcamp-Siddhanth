from sqlalchemy import Table, Column, Integer, String, Float
from app.database import metadata

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("description", String(255)),
    Column("price", Float),
    Column("quantity", Integer),
)

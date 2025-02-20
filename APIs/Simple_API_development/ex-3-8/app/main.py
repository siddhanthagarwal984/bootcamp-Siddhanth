from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Create the "static" directory if it doesn't exist
STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount the static directory so files can be accessed via /static/
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

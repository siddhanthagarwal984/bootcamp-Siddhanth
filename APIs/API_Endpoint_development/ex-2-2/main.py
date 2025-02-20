from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Authentication Example"}

@app.get("/protected")
def protected_route(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password123"

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"message": f"Welcome, {credentials.username}!"}

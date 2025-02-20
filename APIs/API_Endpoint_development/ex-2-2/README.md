# Basic Authentication in FastAPI

## Setup
1. Install dependencies:
   ```bash
   poetry install

2. Run the server:
poetry run uvicorn main:app --reload

3. Test with HTTP Basic Auth using:
curl -u username:password http://127.0.0.1:8000/protected


## Expected Output
If authenticated: "Welcome, username!"
If incorrect credentials: "Unauthorized"
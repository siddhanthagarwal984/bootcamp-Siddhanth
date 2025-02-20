from fastapi import FastAPI, BackgroundTasks
from app.background_tasks import send_email

app = FastAPI()

@app.post("/notify/")
async def notify_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"message": f"Notification will be sent to {email}"}

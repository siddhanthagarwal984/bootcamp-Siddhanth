# Notes on Background Tasks with FastAPI

## Problem Understanding
This script utilizes background tasks in FastAPI to perform operations after returning a response.

## Approach & Methodology
Implement a route that initiates a background task for sending an email notification upon completing a certain action.

## LLMs Used
GPT-4 was used to assist in creating background tasks and handling asynchronous operations.

## Prompts & Responses
**Prompt:**  
How do I use background tasks in FastAPI?

**Response:**  
Use the `BackgroundTasks` class to add tasks that will run after the response is sent.

**Prompt:**  
What is the expected output when notifying a user?

**Response:**  
The API will return a message indicating that the notification will be sent to the specified email.

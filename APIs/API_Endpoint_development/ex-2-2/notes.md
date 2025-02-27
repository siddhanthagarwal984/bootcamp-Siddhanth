# Notes on Basic Authentication with FastAPI

## Problem Understanding
This script secures a FastAPI route with basic authentication.

## Approach & Methodology
Implement basic authentication for one of the routes, requiring a username and password.

## Prompts & Responses
**Prompt:**  
How do I secure a FastAPI route with basic authentication?

**Response:**  
Use the `protected_route` function to implement basic authentication for the route.

**Prompt:**  
What happens if the credentials are invalid?

**Response:**  
The route will return a 401 Unauthorized error if the credentials are invalid.

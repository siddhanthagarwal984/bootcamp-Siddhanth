# Notes on Fetching a User and Their Posts

## Problem Understanding
This script retrieves a user and their associated posts from the database.

## Approach & Methodology
Establish a database session, fetch the user by ID, and retrieve their posts using the defined relationships.

## LLMs Used
GPT-4 was used to assist in creating the logic for fetching users and their posts.

## Prompts & Responses
**Prompt:**  
How do I fetch a user and their posts from the database?

**Response:**  
Use a SQLAlchemy session to query the User model and access the related posts through the defined relationship.

**Prompt:**  
What should I do if no user is found with the given ID?

**Response:**  
Return a message indicating that no user was found with the specified ID.

**Prompt:**  
How can I ensure that the posts are displayed in a structured format?

**Response:**  
Convert the posts to Pydantic models and print their attributes in a readable format.

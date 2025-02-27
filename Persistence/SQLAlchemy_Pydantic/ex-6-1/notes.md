# Notes on Adding a Post Table and Creating a Relationship

## Problem Understanding
This script defines a Post model with a foreign key to the User model, establishing a relationship between them.

## Approach & Methodology
Define the Post model, establish a relationship with the User model, and insert dummy data for testing.

## LLMs Used
GPT-4 was used to assist in creating the Post model and establishing relationships with SQLAlchemy.

## Prompts & Responses
**Prompt:**  
How do I define a relationship between two models in SQLAlchemy?

**Response:**  
Use the relationship() function to define the relationship in the model classes.

**Prompt:**  
What is the purpose of the foreign key in the Post model?

**Response:**  
The foreign key establishes a link between the Post and User models, allowing for relational queries.

**Prompt:**  
How can I insert dummy data for testing the relationship?

**Response:**  
Create instances of User and Post, set the relationships, and add them to the session before committing.

# Notes on Handling Exceptions

## Problem Understanding
This script defines a `ProductManager` class that handles SQLite operations with exception handling for database errors.

## Approach & Methodology
Implement try-except blocks to catch and handle common SQLite errors during database operations.

## LLMs Used
GPT-4 was used to assist in creating the exception handling logic for the ProductManager class.

## Prompts & Responses
**Prompt:**  
How do I handle exceptions in SQLite operations?

**Response:**  
Use try-except blocks around your database operations to catch and handle exceptions.

**Prompt:**  
What types of exceptions should I handle?

**Response:**  
Handle common SQLite errors such as `OperationalError` and `IntegrityError`.

**Prompt:**  
How can I log errors for debugging?

**Response:**  
Print error messages or use a logging framework to log exceptions for later analysis.

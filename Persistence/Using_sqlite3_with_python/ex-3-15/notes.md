# Notes on Batch Insertion

## Problem Understanding
This script defines a `ProductManager` class that handles SQLite operations, including batch insertion of multiple products in one transaction.

## Approach & Methodology
Implement a method that accepts a list of product tuples and inserts them all in one transaction using `executemany()`.

## LLMs Used
GPT-4 was used to assist in creating the batch insertion functionality within the ProductManager class.

## Prompts & Responses
**Prompt:**  
How do I perform batch insertion in SQLite using Python?

**Response:**  
Use the `executemany()` method to insert multiple records in a single database transaction.

**Prompt:**  
What are the benefits of batch insertion?

**Response:**  
Batch insertion reduces the number of database calls, improving performance and efficiency.

**Prompt:**  
How can I handle errors during batch insertion?

**Response:**  
Wrap the insertion logic in a try-except block and rollback the transaction if any error occurs.

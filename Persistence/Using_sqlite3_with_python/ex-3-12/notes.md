# Notes on Join Queries

## Problem Understanding
This script defines a `ProductManager` class that handles SQLite operations, including fetching products along with their categories using join queries.

## Approach & Methodology
Use SQL JOIN statements to combine data from the `products` and `categories` tables based on a common key.

## LLMs Used
GPT-4 was used to assist in creating the join query functionality within the ProductManager class.

## Prompts & Responses
**Prompt:**  
How do I perform a join query in SQLite using Python?

**Response:**  
Use the `JOIN` clause in your SQL statement to combine rows from two or more tables based on a related column.

**Prompt:**  
What is the purpose of foreign keys in join queries?

**Response:**  
Foreign keys establish a relationship between tables, allowing for data integrity and enabling join operations.

**Prompt:**  
How can I handle cases where there are no matching records in a join query?

**Response:**  
Use `LEFT JOIN` to include all records from one table and the matched records from the other, returning `NULL` for non-matching rows.

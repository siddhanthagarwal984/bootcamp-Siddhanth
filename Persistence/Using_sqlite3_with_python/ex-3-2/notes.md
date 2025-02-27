# Notes on Creating a Table

## Problem Understanding
This script creates a table named `products` in the `store.db` database with columns for `id`, `name`, and `price`.

## Approach & Methodology
Use a SQL script to define the table structure and execute it using the `sqlite3` library.

## LLMs Used
GPT-4 was used to assist in creating the table setup script.

## Prompts & Responses
**Prompt:**  
How do I create a table in SQLite using Python?

**Response:**  
Use the `executescript()` method to run a SQL script that defines the table structure.

**Prompt:**  
What does the `IF NOT EXISTS` clause do in the SQL statement?

**Response:**  
This clause prevents an error from occurring if the table already exists in the database.

**Prompt:**  
How can I ensure the table is created with the correct data types?

**Response:**  
Define the data types explicitly in the SQL statement, such as `INTEGER` for `id` and `REAL` for `price`.

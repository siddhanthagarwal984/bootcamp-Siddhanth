# Notes on Inserting Data

## Problem Understanding
This script defines a function to insert a new product into the `products` table in the `store.db` database.

## Approach & Methodology
Use the `sqlite3` library to connect to the database and execute an INSERT statement to add new records.

## LLMs Used
GPT-4 was used to assist in creating the data insertion script.

## Prompts & Responses
**Prompt:**  
How do I insert data into a SQLite table using Python?

**Response:**  
Use the `cursor.execute()` method with an INSERT statement to add new records.

**Prompt:**  
What is the purpose of using placeholders in the INSERT statement?

**Response:**  
Placeholders help prevent SQL injection attacks and ensure proper data formatting.

**Prompt:**  
How can I confirm that the data has been inserted successfully?

**Response:**  
Print a confirmation message after the `commit()` method is called.

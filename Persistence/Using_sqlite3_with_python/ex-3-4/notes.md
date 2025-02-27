# Notes on Reading Data

## Problem Understanding
This script fetches and prints all records from the `products` table in the `store.db` database.

## Approach & Methodology
Use the `sqlite3` library to connect to the database and execute a SELECT statement to retrieve records.

## LLMs Used
GPT-4 was used to assist in creating the data retrieval script.

## Prompts & Responses
**Prompt:**  
How do I fetch data from a SQLite table using Python?

**Response:**  
Use the `cursor.execute()` method with a SELECT statement to retrieve records.

**Prompt:**  
What should I do if no records are found?

**Response:**  
Print a message indicating that no products were found in the table.

**Prompt:**  
How can I format the output of the fetched records?

**Response:**  
Iterate through the records and print each field in a readable format.

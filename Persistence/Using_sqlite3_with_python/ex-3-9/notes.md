# Notes on Search Functionality

## Problem Understanding
This script defines a method to search for products by name fragment in the `products` table of the `store.db` database.

## Approach & Methodology
Use the `sqlite3` library to connect to the database and execute a SELECT statement with a LIKE clause to find matching records.

## LLMs Used
GPT-4 was used to assist in creating the search functionality within the ProductManager class.

## Prompts & Responses
**Prompt:**  
How do I search for records in a SQLite table using Python?

**Response:**  
Use the `cursor.execute()` method with a SELECT statement that includes a LIKE clause to filter results.

**Prompt:**  
What is the purpose of using wildcards in the search query?

**Response:**  
Wildcards allow for flexible matching of strings, enabling partial matches based on user input.

**Prompt:**  
How can I handle cases where no products match the search criteria?

**Response:**  
Check the results and print a message indicating that no matching products were found.

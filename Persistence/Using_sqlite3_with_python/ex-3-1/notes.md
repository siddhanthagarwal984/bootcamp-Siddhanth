# Notes on Setting Up SQLite Database

## Problem Understanding
This script connects to a SQLite database named `store.db` and creates it if it doesn't exist.

## Approach & Methodology
Use the `sqlite3` library to establish a connection to the database and close it after creation.

## LLMs Used
GPT-4 was used to assist in creating the database setup script.

## Prompts & Responses
**Prompt:**  
How do I create a SQLite database in Python?

**Response:**  
Use the `sqlite3.connect()` method to create a connection to the database file.

**Prompt:**  
What happens if the database already exists?

**Response:**  
The connection will simply open the existing database without creating a new one.

**Prompt:**  
How do I ensure the connection is properly closed?

**Response:**  
Always call `conn.close()` after completing your database operations.

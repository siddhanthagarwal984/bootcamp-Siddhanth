# Notes on Basic Transaction Handling

## Problem Understanding
This script defines a function to insert multiple customer records into a database using transactions, ensuring data integrity.

## Approach & Methodology
Wrap the insertion logic in a transaction to commit all changes only if all operations succeed, rolling back in case of errors.

## LLMs Used
GPT-4 was used to assist in creating the transaction handling logic for inserting customer records.

## Prompts & Responses
**Prompt:**  
How do I implement basic transaction handling in SQLite using Python?

**Response:**  
Use `BEGIN TRANSACTION;` before your operations and `commit()` after to finalize changes.

**Prompt:**  
What should I do if an error occurs during the transaction?

**Response:**  
Use a try-except block to catch exceptions and call `rollback()` to revert changes if an error occurs.

**Prompt:**  
How can I ensure that all records are inserted successfully?

**Response:**  
Wrap all insert operations in a single transaction to ensure that either all changes are applied or none at all.

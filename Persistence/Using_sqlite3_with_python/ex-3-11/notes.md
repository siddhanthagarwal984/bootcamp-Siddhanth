# Notes on Using Transactions

## Problem Understanding
This script defines a `ProductManager` class that handles SQLite operations with transaction management for data integrity.

## Approach & Methodology
Wrap database operations in transactions to ensure that all changes are committed only if all operations succeed.

## LLMs Used
GPT-4 was used to assist in creating the transaction management logic for the ProductManager class.

## Prompts & Responses
**Prompt:**  
How do I implement transactions in SQLite using Python?

**Response:**  
Use the `BEGIN TRANSACTION;` statement before your operations and `commit()` after to finalize changes.

**Prompt:**  
What should I do if an error occurs during a transaction?

**Response:**  
Use a try-except block to catch exceptions and call `rollback()` to revert changes if an error occurs.

**Prompt:**  
How can I ensure data integrity during multiple database operations?

**Response:**  
Wrap all related operations in a single transaction to ensure that either all changes are applied or none at all.

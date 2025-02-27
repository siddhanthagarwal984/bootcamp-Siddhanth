# Notes on Using Transactions for Bulk Inserts

## Problem Understanding
This script performs bulk inserts of users into the database using SQLAlchemy transactions.

## Approach & Methodology
Establish a database session, prepare user data, and use a transaction to insert multiple users at once.

## LLMs Used
GPT-4 was used to assist in creating the logic for bulk inserts with transaction management.

## Prompts & Responses
**Prompt:**  
How do I perform a bulk insert in SQLAlchemy?

**Response:**  
Use a session to add multiple instances of the model and commit them in a single transaction.

**Prompt:**  
What happens if one of the inserts fails?

**Response:**  
Implement error handling to rollback the transaction and prevent partial inserts.

**Prompt:**  
How can I ensure that the data being inserted is valid?

**Response:**  
Validate the data using Pydantic schemas before performing the bulk insert.

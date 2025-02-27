# Notes on Using a Class

## Problem Understanding
This script defines a `ProductManager` class to handle SQLite operations for the `products` table.

## Approach & Methodology
Encapsulate database operations within a class to manage products, including creating the table and adding new products.

## LLMs Used
GPT-4 was used to assist in creating the class structure for managing products.

## Prompts & Responses
**Prompt:**  
How do I encapsulate database operations in a class?

**Response:**  
Define methods within a class that perform specific database operations, such as adding or updating records.

**Prompt:**  
What are the benefits of using a class for database operations?

**Response:**  
Encapsulation improves code organization, reusability, and maintainability by grouping related functionality.

**Prompt:**  
How can I ensure that the table is created when the class is instantiated?

**Response:**  
Call the table creation method in the constructor of the class to ensure it runs upon instantiation.

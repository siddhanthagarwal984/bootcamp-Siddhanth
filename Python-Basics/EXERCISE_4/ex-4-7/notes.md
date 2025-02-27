# ex-4-7: Retry Mechanism Decorator

## Problem Understanding
Implement a decorator to retry a function.

## Approach & Methodology
- Develop a `retry` decorator that retries a function up to a specified number of times if it raises an exception.
- Demonstrate how to apply the decorator to a sample function.
- Explain the flow of execution and how retries are handled.

## LLMs Used
GPT-4 was used to assist in implementing a retry mechanism decorator.

## Prompts & Responses
**Prompt:**  
How can I create a retry mechanism decorator in Python?

**Response:**  
Use a loop to call the function and catch exceptions, retrying until the maximum number of attempts is reached.

**Prompt:**  
What should happen if the function succeeds on a retry?

**Response:**  
The decorator should return the result of the function call immediately without further retries.

# ex-4-4: Memoization Decorator

## Problem Understanding
Create a decorator for caching function results.

## Approach & Methodology
- Write a `memoize` decorator that caches the return values of a function, so repeated calls with the same arguments return the cached result.
- Demonstrate how to apply the decorator to a sample function.
- Explain the flow of execution and how caching is handled.

## LLMs Used
GPT-4 was used to assist in creating a memoization decorator.

## Prompts & Responses
**Prompt:**  
How can I create a memoization decorator in Python?

**Response:**  
Use a dictionary to store the results of function calls based on the input arguments.

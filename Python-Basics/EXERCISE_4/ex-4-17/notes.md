# ex-4-17: functools.lru_cache for Optimization

## Problem Understanding
Optimize a recursive function with lru_cache.

## Approach & Methodology
- Write a recursive function to calculate Fibonacci numbers and use `functools.lru_cache` to optimize it.
- Demonstrate how to apply lru_cache in a sample code.
- Explain the flow of execution and how caching improves performance.

## LLMs Used
GPT-4 was used to assist in optimizing a recursive function with lru_cache.

## Prompts & Responses
**Prompt:**  
How can I use functools.lru_cache to optimize a recursive Fibonacci function?

**Response:**  
Decorate the Fibonacci function with `@lru_cache(maxsize=None)` to cache results of previous calls.

**Prompt:**  
What are the benefits of using lru_cache?

**Response:**  
It significantly reduces the time complexity of recursive functions by storing previously computed results.

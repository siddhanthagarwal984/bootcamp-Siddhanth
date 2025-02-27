# ex-4-19: functools.total_ordering for Classes

## Problem Understanding
Use total_ordering to simplify class comparison.

## Approach & Methodology
- Create a class representing a simple 2D point (with x and y coordinates) and use `functools.total_ordering` to compare points based on their distance from the origin.
- Demonstrate how to apply total_ordering in a sample code.
- Explain the flow of execution and how total_ordering simplifies comparisons.

## LLMs Used
GPT-4 was used to assist in implementing functools.total_ordering.

## Prompts & Responses
**Prompt:**  
How can I use functools.total_ordering to compare instances of a class in Python?

**Response:**  
Decorate the class with `@total_ordering` and define `__lt__` and `__eq__` methods to enable comparison.

**Prompt:**  
What are the benefits of using total_ordering?

**Response:**  
It reduces boilerplate code by automatically providing the missing comparison methods based on the defined ones.

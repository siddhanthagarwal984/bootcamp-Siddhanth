# ex-4-20: Combining functools with List Comprehensions

## Problem Understanding
Integrate functools with list comprehensions.

## Approach & Methodology
- Use `functools.reduce` along with a list comprehension to calculate the sum of squares of numbers from 1 to 10.
- Demonstrate how to apply reduce in a sample code.
- Explain the flow of execution and how functools integrates with list comprehensions.

## LLMs Used
GPT-4 was used to assist in combining functools with list comprehensions.

## Prompts & Responses
**Prompt:**  
How can I use functools.reduce with a list comprehension to calculate the sum of squares?

**Response:**  
Use the syntax `reduce(lambda x, y: x + y, [x**2 for x in range(1, 11)])` to calculate the sum of squares from 1 to 10.

**Prompt:**  
What are the advantages of combining functools with list comprehensions?

**Response:**  
It allows for efficient and concise operations on collections, leveraging both functional programming and list processing capabilities.

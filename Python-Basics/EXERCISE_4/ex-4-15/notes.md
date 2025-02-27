# ex-4-15: Combining functools.reduce with Lambda

## Problem Understanding
Implement reduce with a lambda function.

## Approach & Methodology
- Utilize `functools.reduce` and a lambda function to calculate the factorial of a number.
- Demonstrate how to apply reduce in a sample code.
- Explain the flow of execution and how reduce works with lambda functions.

## LLMs Used
GPT-4 was used to assist in implementing functools.reduce with a lambda function.

## Prompts & Responses
**Prompt:**  
How can I use functools.reduce with a lambda function to calculate a factorial in Python?

**Response:**  
Use `reduce(lambda x, y: x * y, range(1, n + 1))` to calculate the factorial of `n`.

**Prompt:**  
What are the advantages of using reduce with lambda functions?

**Response:**  
They allow for concise and functional-style programming, making it easier to apply operations across a sequence of elements.

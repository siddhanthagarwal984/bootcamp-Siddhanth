# ex-5-4: Using Dunder Methods

## Problem Understanding
Implement the `__str__` and `__repr__` methods for the Book class.

## Approach & Methodology
- Create instances and print them to see the effect of these methods.
- Explain how dunder methods enhance the usability of class instances.
- Provide examples of how these methods can be overridden.

## LLMs Used
GPT-4 was used to assist in implementing dunder methods for the Book class.

## Prompts & Responses
**Prompt:**  
How can I implement the `__str__` and `__repr__` methods in the Book class?

**Response:**  
Define the methods to return a string representation of the object for user-friendly and developer-friendly outputs, respectively.

**Prompt:**  
What is the difference between `__str__` and `__repr__`?

**Response:**  
`__str__` is meant for creating a readable string for end-users, while `__repr__` is intended for developers and should ideally be unambiguous.

**Prompt:**  
Can I customize the output of print statements for my class instances?

**Response:**  
Yes, by implementing `__str__` and `__repr__`, you can customize how instances are represented in print statements.

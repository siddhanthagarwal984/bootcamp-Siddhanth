# ex-5-12: Enforcing Interface Implementation

## Problem Understanding
Create an interface using ABC and enforce its implementation in subclasses.

## Approach & Methodology
- Create an interface Streamable with method stream() and subclasses like VideoStream and AudioStream.
- Explain how to enforce interface implementation in subclasses.
- Provide examples of how interfaces can be used to define a contract for subclasses.

## LLMs Used
GPT-4 was used to assist in creating an interface and enforcing its implementation.

## Prompts & Responses
**Prompt:**  
How can I create an interface using ABC in Python?

**Response:**  
Use the `abc` module and define an abstract class with abstract methods.

**Prompt:**  
What is the purpose of using interfaces?

**Response:**  
Interfaces define a contract that implementing classes must follow, ensuring consistency.

**Prompt:**  
Can I have multiple subclasses implementing the same interface?

**Response:**  
Yes, multiple subclasses can implement the same interface, each providing its own implementation.

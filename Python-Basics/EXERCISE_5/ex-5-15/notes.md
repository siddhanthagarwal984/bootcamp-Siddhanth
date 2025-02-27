# ex-5-15: Immutable Class

## Problem Understanding
Create an immutable class where instances cannot be modified after creation.

## Approach & Methodology
- Implement a Point class representing a point in 2D space.
- Explain how to enforce immutability in class design.
- Provide examples of creating and using immutable instances.

## LLMs Used
GPT-4 was used to assist in creating an immutable class.

## Prompts & Responses
**Prompt:**  
How can I create an immutable class in Python?

**Response:**  
Use `__slots__` to prevent attribute assignment and avoid setter methods.

**Prompt:**  
What are the benefits of immutability?

**Response:**  
Immutability can lead to safer code, easier debugging, and better performance in certain scenarios.

**Prompt:**  
Can I create methods in an immutable class?

**Response:**  
Yes, you can create methods, but they cannot modify the instance's attributes.

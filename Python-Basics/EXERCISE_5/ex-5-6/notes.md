# ex-5-6: Contracts with @property

## Problem Understanding
Implement a Temperature class that strictly controls setting and getting temperature values using @property.

## Approach & Methodology
- Enforce a range for temperature values (e.g., -273.15°C to 5000°C).
- Demonstrate how to use the @property decorator to manage access to the temperature attribute.
- Explain the flow of execution and how property methods work.

## LLMs Used
GPT-4 was used to assist in implementing the Temperature class with property decorators.

## Prompts & Responses
**Prompt:**  
How can I implement a Temperature class with @property?

**Response:**  
Use the @property decorator to create getter and setter methods for the temperature attribute.

**Prompt:**  
What happens if I try to set a temperature below -273.15°C?

**Response:**  
You should raise a ValueError to enforce the temperature limit.

**Prompt:**  
Can I use @property to enforce read-only attributes?

**Response:**  
Yes, by only defining a getter method and not providing a setter, you can create a read-only property.

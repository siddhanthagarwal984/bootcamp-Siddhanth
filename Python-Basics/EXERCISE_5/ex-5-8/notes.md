# ex-5-8: Abstract Properties

## Problem Understanding
Add abstract properties to an abstract base class and implement them in child classes.

## Approach & Methodology
- Create an abstract class Animal with an abstract property sound.
- Implement the sound property in derived classes like Dog and Cat.
- Explain how abstract properties enforce a contract for subclasses.

## LLMs Used
GPT-4 was used to assist in creating abstract properties in the Animal class.

## Prompts & Responses
**Prompt:**  
How can I add abstract properties to an abstract base class?

**Response:**  
Use the `abc` module and define an abstract property using the `@property` and `@abstractmethod` decorators.

**Prompt:**  
What is the purpose of abstract properties?

**Response:**  
They ensure that derived classes implement specific properties, enforcing a consistent interface.

**Prompt:**  
Can I have multiple abstract properties in a single abstract class?

**Response:**  
Yes, you can define multiple abstract properties in an abstract class.

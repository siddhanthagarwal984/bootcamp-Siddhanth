# ex-5-5: Implementing an Abstract Base Class (ABC)

## Problem Understanding
Create an abstract base class Shape with an abstract method area.

## Approach & Methodology
- Derive subclasses like Circle and Rectangle, implementing area in each.
- Explain how abstract base classes work and their use cases.
- Provide examples of calculating the area for different shapes.

## LLMs Used
GPT-4 was used to assist in creating an abstract base class and its subclasses.

## Prompts & Responses
**Prompt:**  
How can I create an abstract base class in Python?

**Response:**  
Use the `abc` module and define an abstract method using the `@abstractmethod` decorator.

**Prompt:**  
What is the purpose of an abstract base class?

**Response:**  
It provides a blueprint for other classes to implement specific methods, ensuring a consistent interface.

**Prompt:**  
Can I instantiate an abstract base class directly?

**Response:**  
No, abstract base classes cannot be instantiated directly; they must be subclassed.

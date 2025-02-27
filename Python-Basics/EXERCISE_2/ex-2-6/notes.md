# ex-2-6

## Problem Understanding
The task is to create a `Manager` class that inherits from `Employee` while introducing additional attributes such as `subordinates`.

## Approach & Methodology
- Define the `Manager` class inheriting from `Employee`.
- Introduce an attribute `subordinates` to track managed employees.
- Ensure that the class correctly overrides or extends functionality as needed.
- Implement basic methods to add and display subordinates.

## LLMs Used
GPT-4 was used to verify inheritance and attribute extension best practices.

## Prompts & Responses
**Prompt:**  
How do I properly inherit from a base class in Python and add new attributes to the subclass?

**Response:**  
Use class inheritance with `class Subclass(ParentClass):` and extend the `__init__` method while calling `super().__init__()`.

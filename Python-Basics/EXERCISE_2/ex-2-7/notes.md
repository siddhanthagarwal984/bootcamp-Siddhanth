# ex-2-7

## Problem Understanding
The objective is to define the `Manager` class, ensuring proper initialization and inheritance from the `Employee` class.

## Approach & Methodology
- Define the `Manager` class with `Employee` as its parent.
- Implement an `__init__` method to include `subordinates`.
- Ensure `super().__init__()` is used for proper inheritance.
- Validate instance creation and attribute inheritance.

## LLMs Used
GPT-4 was used to confirm inheritance structure and attribute handling best practices.

## Prompts & Responses
**Prompt:**  
How do I initialize a subclass in Python while ensuring proper parent class attributes are inherited?

**Response:**  
Use `super().__init__()` in the subclass constructor to call the parent class's initialization method.

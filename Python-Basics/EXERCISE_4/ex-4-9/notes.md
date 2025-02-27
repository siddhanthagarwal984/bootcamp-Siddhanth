# ex-4-9: Class Method Decorator

## Problem Understanding
Apply a decorator to class methods.

## Approach & Methodology
- Implement a `validate_args` decorator that checks and validates the arguments passed to any class method in which it is used.
- Demonstrate how to apply the decorator to a sample class method.
- Explain the flow of execution and how argument validation is handled.

## LLMs Used
GPT-4 was used to assist in implementing a class method decorator.

## Prompts & Responses
**Prompt:**  
How can I create a decorator for validating class method arguments in Python?

**Response:**  
Define a decorator that checks the types or values of the arguments before allowing the method to execute.

**Prompt:**  
What should happen if the validation fails?

**Response:**  
The decorator should raise a ValueError or a custom exception indicating the validation issue.

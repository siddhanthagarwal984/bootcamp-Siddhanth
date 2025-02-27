# ex-4-6: Access Control Decorator

## Problem Understanding
Write a decorator to restrict access to a function.

## Approach & Methodology
- Create a `role_required` decorator that takes a user role and only allows the function to execute if the provided user has the specified role.
- Demonstrate how to apply the decorator to a sample function.
- Explain the flow of execution and how access control is enforced.

## LLMs Used
GPT-4 was used to assist in writing an access control decorator.

## Prompts & Responses
**Prompt:**  
How can I create an access control decorator in Python?

**Response:**  
Define a decorator that checks the user's role before allowing the function to execute.

**Prompt:**  
What should happen if the user does not have the required role?

**Response:**  
The decorator should raise an exception or return an error message indicating insufficient permissions.

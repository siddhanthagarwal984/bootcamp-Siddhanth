# ex-5-16: Custom Context Managers

## Problem Understanding
Create a custom context manager using the `__enter__` and `__exit__` methods to handle file operations gracefully.

## Approach & Methodology
- Implement the `FileOpen` class that opens a file in a specified mode and ensures it is closed after use.
- Provide an example of how to use the `FileOpen` context manager in a script.

## Prompts & Responses
**1. How does a context manager work in Python?**  
A context manager in Python is used to allocate and release resources precisely when you want to. The `with` statement is used to wrap the execution of a block with methods defined by a context manager.

**2. What are the advantages of using context managers?**  
Context managers help in resource management, ensuring that resources are properly cleaned up after use, even if an error occurs. They make the code cleaner and more readable.

**3. Can you nest context managers?**  
Yes, you can nest context managers by using multiple `with` statements or by using a single `with` statement to manage multiple context managers.

**4. How do you handle exceptions in a context manager?**  
You can handle exceptions in the `__exit__` method of the context manager. You can check the exception type and handle it accordingly.

**5. What happens if an exception occurs in the `__enter__` method?**  
If an exception occurs in the `__enter__` method, the context manager will not be entered, and the exception will propagate up to the caller.

**6. How can you create a context manager without using classes?**  
You can use the `contextlib` module's `contextmanager` decorator to create a context manager using a generator function.

## LLMs Used
GPT-4 was used for initial problem analysis and solution design.
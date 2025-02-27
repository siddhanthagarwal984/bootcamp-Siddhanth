# Notes for ex-1-2

## 1. Understanding of the Problem
The goal of this exercise is to create a command-line interface (CLI) using Typer that imports 
a function from the "helloworld" module and prints a greeting message. The function 
`say_hello(name)` should return "Hello, {name}" and the CLI should accept a 
name as an argument and display the message.

## 2. Approach Taken
- First, created a new folder `ex-1-2`.
- Created a Python package with the structure:
    ```
    ex-1-2/
    ├── helloworld/
    │   ├── __init__.py
    │   ├── hello.py
    │   ├── main.py
    ```
- Implemented `say_hello()` in `sayhello.py`.
- Created `main.py` that uses Typer for CLI interaction.
- Tested the CLI using command-line execution.

## 3. LLMs Used and Their Content
ChatGPT 4 provided insights into:
- How to structure a Python package.
- How to use Typer for CLI applications.
- Best practices for modular Python code.

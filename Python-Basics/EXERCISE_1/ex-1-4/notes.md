# Notes for ex-1-4: many-hellos CLI

## 1. Understanding of the Problem
The goal is to create a CLI tool that greets multiple names one by one using the `say_hello` 
function from the "helloworld" package.

## 2. Approach Taken
- Created a new project `many-hellos` with Poetry.
- Imported `say_hello` from the `helloworld` package.
- Implemented a CLI using `Typer` to accept multiple names.
- Tested it using:
    ```
    python -m many_hellos.cli Alice Bob Charlie
    ```

## 3. LLMs Used and Their Content
ChatGPT 4 was used to:
- Ensure proper CLI argument parsing for multiple names.
- Resolve issues related to package imports across different projects.
- Test CLI behavior for empty inputs.

## 4. Prompts and Responses
**1. How to pass multiple arguments in Typer?**  
Use:
```python
def main(names: List[str]):
```

**2. How to test the CLI?**  
Run:
```
python -m many_hellos.cli Alice Bob Charlie

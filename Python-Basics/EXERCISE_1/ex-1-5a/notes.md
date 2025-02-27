# Notes for ex-1-5a: Using Config YAML for num_times

## 1. Understanding of the Problem
The goal is to extend the `say_hello` function to load a `_config.yaml` file that contains 
a parameter called `num_times`. This parameter determines how many times the greeting 
should be repeated.

## 2. Approach Taken
- Added a `_config.yaml` file with the `num_times` parameter.
- Modified `say_hello.py` to read from this config file.
- Tested by calling the function and verifying the output.

## 3. LLMs Used and Their Content
ChatGPT 4 was used to:
- Understand how to read YAML files in Python.
- Determine best practices for handling missing config files.
- Debug file path resolution issues.

## 4. Prompts and Responses
**1. How to load a YAML file in Python?**  
Use:
```python
import yaml
with open("_config.yaml", "r") as file:
    config = yaml.safe_load(file)

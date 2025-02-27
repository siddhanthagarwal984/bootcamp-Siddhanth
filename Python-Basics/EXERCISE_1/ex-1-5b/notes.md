# Notes for ex-1-5b: Search YAML in Multiple Paths

## 1. Understanding of the Problem
The goal is to enhance `say_hello.py` so that it searches for `_config.yaml` in:
- The current directory
- Paths listed in the `CONFIG_PATH` environment variable
- A default YAML file in the package

## 2. Approach Taken
- Implemented a search mechanism using `os.environ`.
- Handled cases where the config file is missing.
- Tested different scenarios (current directory, environment variable, default file).

## 3. LLMs Used and Their Content
ChatGPT 4 was used to:
- Implement the multi-path search logic efficiently.
- Handle potential permission and path issues.

## 4. Prompts and Responses
**1. How to read an environment variable in Python?**  
Use:
```python
import os
path = os.environ.get("CONFIG_PATH")

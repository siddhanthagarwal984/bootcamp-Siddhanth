# Notes for ex-1-6: Adding Logging to say_hello and config_loader

## 1. Understanding of the Problem
The goal is to add logging to both `say_hello` and `config_loader.py`. 
This helps track when configuration files are loaded and when the 
`say_hello` function is called.

## 2. Approach Taken
- Used Python's built-in `logging` library.
- Added logging at key points: when loading configs and when executing the greeting logic.
- Configured logging at the `INFO` level.
- Tested the logs by running the CLI.

## 3. LLMs Used and Their Content
ChatGPT 4 was used to:
- Understand how to add logging to Python functions.
- Implement per-module logging for `config_loader.py` and `hello.py`.
- Ensure logs followed a clean format.

## 4. Prompts and Responses
**1. How to add logging to a Python module?**  
Use:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

**2. How to log config loading?**  
In `config_loader.py`, I added:
```python
logger.info(f"Loading config from {config_path}")
```

**3. How to run the CLI and see the logs?**  
Run:
```bash
python -m hello.hello

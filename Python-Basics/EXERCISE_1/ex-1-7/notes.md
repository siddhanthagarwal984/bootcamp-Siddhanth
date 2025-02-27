# Notes for ex-1-7: Enable Logging for many-hellos

## 1. Understanding of the Problem
The goal is to enable logging in the CLI application `many-hellos`, ensuring that 
logs from both the `say_hello` function and `config_loader.py` are visible when the CLI is executed.

## 2. Approach Taken
- Added `logging.basicConfig(level=logging.INFO)` to `cli.py`.
- Ensured logs from both modules appeared when running the CLI.

## 3. LLMs Used and Their Content
ChatGPT 4 was used to:
- Enable logging across modules in a CLI tool.
- Ensure logs appeared in a clean, readable format.

## 4. Prompts and Responses
**1. How to enable logging for the CLI?**  
Add this to `cli.py`:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

**2. How to run the CLI and see the logs?**  
Run:
```bash
python -m many_hellos.cli Alice Bob

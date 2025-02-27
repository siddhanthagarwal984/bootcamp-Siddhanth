# Notes for ex-1-8: Disable Logging

## 1. Understanding of the Problem
The goal is to disable logging for `many-hellos`, ensuring that no logs are shown when running the CLI.

## 2. Approach Taken
- Used `logging.basicConfig(level=logging.CRITICAL)` to suppress logs.
- Tested the CLI to confirm no logs appeared.

## 3. Prompts and Responses
**1. How to disable logging in Python?**  
Set logging level to CRITICAL:
```python
logging.basicConfig(level=logging.CRITICAL)
```

**2. How to test if logs are suppressed?**  
Run:
```bash
python -m many_hellos.cli Alice Bob
```
No logs should appear — only the "Hello" messages.

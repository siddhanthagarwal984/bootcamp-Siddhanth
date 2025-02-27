# Notes for ex-1-9: Selective Logging for config_loader

## 1. Understanding of the Problem
The goal is to enable logging only for `config_loader.py` while suppressing logs from other modules.

## 2. Approach Taken
- Used `logging.getLogger("hello.config_loader").setLevel(logging.INFO)`.

## 3. Prompts and Responses
**1. How to enable selective logging?**  
Use:
```python
logging.getLogger("hello.config_loader").setLevel(logging.INFO)
```

**2. How to verify only config logs show?**  
Run:
```bash
python -m many_hellos.cli Alice
```
Expect only config loading logs to appear.

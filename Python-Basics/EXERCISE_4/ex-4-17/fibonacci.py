from functools import lru_cache

@lru_cache(maxsize=None)  # Cache all Fibonacci calculations
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion with caching."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

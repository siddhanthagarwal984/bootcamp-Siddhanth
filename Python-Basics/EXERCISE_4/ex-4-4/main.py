from decorators import memoize

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # First call calculates
print(fibonacci(10))  # Second call fetches from cache

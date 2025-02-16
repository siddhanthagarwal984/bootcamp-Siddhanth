from functools import reduce

def factorial(n):
    """Calculate the factorial of a number using functools.reduce and a lambda function."""
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))
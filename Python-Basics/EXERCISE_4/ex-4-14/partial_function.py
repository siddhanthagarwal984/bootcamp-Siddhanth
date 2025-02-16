from functools import partial

def multiply(a, b):
    """Generic multiplication function."""
    return a * b

# Create a partial function that always multiplies by 2
double = partial(multiply, 2)
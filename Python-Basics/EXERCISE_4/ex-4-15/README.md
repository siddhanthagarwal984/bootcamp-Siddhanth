# Combining functools.reduce with Lambda

## Problem
Use `functools.reduce` and a lambda function to calculate the factorial of a number.

## Solution
Using `reduce` to multiply all numbers in a range:
```python
reduce(lambda x, y: x * y, range(1, n + 1))

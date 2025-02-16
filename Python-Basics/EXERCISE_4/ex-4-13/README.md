# Nested List Comprehension

## Problem
Flatten a matrix (list of lists) into a single list using nested list comprehension.

## Solution
Using a nested list comprehension:
```python
[num for row in matrix for num in row]

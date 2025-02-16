# functools.total_ordering for Classes

## Problem Statement
Create a class representing a simple 2D point (with x and y coordinates) and use functools.total_ordering to compare points based on their distance from the origin.

## Solution
- The `Point` class defines `x` and `y` coordinates.
- The `distance_from_origin` method calculates the Euclidean distance.
- `functools.total_ordering` simplifies comparison logic by requiring only `__eq__` and `__lt__` to be implemented.

## Example Output

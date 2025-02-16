from functools import reduce

def sum_of_squares(n):
    """Returns the sum of squares of numbers from 1 to n using functools.reduce."""
    return reduce(lambda x, y: x + y, [x ** 2 for x in range(1, n + 1)])

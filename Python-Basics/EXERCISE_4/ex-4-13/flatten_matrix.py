def flatten_matrix(matrix):
    """Flatten a matrix (list of lists) into a single list using nested list comprehension."""
    return [num for row in matrix for num in row]
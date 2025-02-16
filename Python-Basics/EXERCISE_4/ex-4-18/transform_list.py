def transform_list(input_list):
    """Transforms strings to uppercase and squares integers in a list."""
    return [x.upper() if isinstance(x, str) else x ** 2 for x in input_list]

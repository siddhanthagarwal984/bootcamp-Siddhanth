def generate_even_numbers():
    """Generate a list of even numbers from 1 to 20."""
    return [x for x in range(1, 21) if x % 2 == 0]
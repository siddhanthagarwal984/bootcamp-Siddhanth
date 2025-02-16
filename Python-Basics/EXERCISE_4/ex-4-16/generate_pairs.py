def generate_pairs(list1, list2):
    """Returns all possible pairs (as tuples) of numbers from two lists."""
    return [(x, y) for x in list1 for y in list2]

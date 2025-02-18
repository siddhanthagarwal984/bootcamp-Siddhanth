from itertools import chain

def combined_iterators(*iterators):
    return chain(*iterators)

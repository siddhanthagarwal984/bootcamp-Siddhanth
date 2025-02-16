from decorators import debug_info

@debug_info
def add(a, b):
    return a + b

add(3, 5)

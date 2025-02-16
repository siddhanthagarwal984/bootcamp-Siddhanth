class Point:
    """Immutable 2D point class."""

    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, key, value):
        raise AttributeError("Cannot modify immutable instance")

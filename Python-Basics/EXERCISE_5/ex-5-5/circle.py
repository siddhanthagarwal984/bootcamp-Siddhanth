import math
from shape import Shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Computes the area of a circle."""
        return math.pi * self.radius ** 2

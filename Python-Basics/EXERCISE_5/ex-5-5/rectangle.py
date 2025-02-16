from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        """Computes the area of a rectangle."""
        return self.width * self.height

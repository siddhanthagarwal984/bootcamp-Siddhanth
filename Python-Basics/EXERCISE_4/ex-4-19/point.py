from functools import total_ordering
import math

@total_ordering
class Point:
    """Represents a 2D point and allows comparison based on distance from origin."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Returns the Euclidean distance of the point from the origin (0,0)."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

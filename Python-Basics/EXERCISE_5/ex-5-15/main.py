from point import Point

p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")

try:
    p.x = 5
except AttributeError as e:
    print(f"Error: {e}")

from point import Point

if __name__ == "__main__":
    p1 = Point(3, 4)  # Distance from origin = 5
    p2 = Point(6, 8)  # Distance from origin = 10

    print(f"{p1} < {p2}: {p1 < p2}")   # True
    print(f"{p1} > {p2}: {p1 > p2}")   # False
    print(f"{p1} == {p2}: {p1 == p2}") # False

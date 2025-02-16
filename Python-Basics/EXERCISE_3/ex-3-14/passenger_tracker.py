from collections import defaultdict

# Default dictionary for tracking passengers per station
passenger_count = defaultdict(int)

# Simulating passenger entries
passenger_count["Station A"] += 5
passenger_count["Station B"] += 3
passenger_count["Station C"] += 8

# Accessing a missing station
print("Passengers at Station X:", passenger_count["Station X"])  # Returns 0 instead of an error
print("Passenger Count:", passenger_count)

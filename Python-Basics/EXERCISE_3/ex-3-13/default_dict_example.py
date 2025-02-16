from collections import defaultdict

# Default dictionary with a default value of an empty list
transport_schedule = defaultdict(list)

# Adding bus stops
transport_schedule["Route 1"].append(("08:00", "Station A"))
transport_schedule["Route 1"].append(("08:15", "Station B"))

# Accessing a missing key
print("Route 2 schedule:", transport_schedule["Route 2"])  # Returns an empty list instead of an error

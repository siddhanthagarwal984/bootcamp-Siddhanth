from collections import defaultdict

# Nested defaultdict structure for transportation data
transport_data = defaultdict(lambda: defaultdict(list))

# Adding data
transport_data["Bus"]["Route 1"].append(("08:00", "Station A"))
transport_data["Train"]["Red Line"].append(("07:30", "Station G"))

print("Complex Nested Transport Data:", transport_data)

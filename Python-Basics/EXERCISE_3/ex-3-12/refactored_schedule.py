from collections import namedtuple

# Define the named tuple
Schedule = namedtuple("Schedule", ["time", "station"])

# Refactored schedule using named tuples
route_schedule = {
    "Route 1": [Schedule("08:00", "Station A"), Schedule("08:15", "Station B"), Schedule("08:30", "Station C")],
    "Red Line": [Schedule("07:30", "Station G"), Schedule("07:45", "Station H"), Schedule("08:00", "Station I")]
}

print("Refactored Route Schedule:", route_schedule)

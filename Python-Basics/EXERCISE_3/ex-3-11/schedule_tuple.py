from collections import namedtuple

# Define a named tuple for transportation schedules
Schedule = namedtuple("Schedule", ["time", "station"])

# Example usage
example_schedule = Schedule("08:00", "Station A")
print("Example Schedule:", example_schedule)

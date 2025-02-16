from collections import namedtuple

# Define a named tuple for transportation schedules
Stop = namedtuple("Stop", ["time", "station"])
Route = namedtuple("Route", ["name", "stops"])

# Create structured data using named tuples
bus_route = Route("Route 1", [Stop("08:00", "Station A"), Stop("08:15", "Station B")])
train_line = Route("Red Line", [Stop("07:30", "Station G"), Stop("07:45", "Station H")])

print("Bus Route:", bus_route)
print("Train Line:", train_line)

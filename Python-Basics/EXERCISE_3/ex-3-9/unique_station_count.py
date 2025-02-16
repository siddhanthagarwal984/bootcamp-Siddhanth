from schedule import schedule

# Extract all stations from the schedule
bus_stations = {stop[1] for route in schedule["Bus Routes"].values() for stop in route}
train_stations = {stop[1] for line in schedule["Train Lines"].values() for stop in line}

# Calculate unique stations
unique_stations = bus_stations.union(train_stations)
print("Total Unique Stations:", len(unique_stations))

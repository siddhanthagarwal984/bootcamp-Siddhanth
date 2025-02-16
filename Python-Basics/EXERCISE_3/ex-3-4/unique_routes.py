# Using sets to store unique transportation routes
bus_routes = {"Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6"}
train_lines = {"Red Line", "Blue Line", "Green Line"}

unique_routes = bus_routes.union(train_lines)
print("Unique Transportation Routes:", unique_routes)

# Nested data structure to represent transportation schedules
schedule = {
    "Bus Routes": {
        "Route 1": [("08:00", "Station A"), ("08:15", "Station B"), ("08:30", "Station C")],
        "Route 2": [("09:00", "Station D"), ("09:20", "Station E"), ("09:40", "Station F")]
    },
    "Train Lines": {
        "Red Line": [("07:30", "Station G"), ("07:45", "Station H"), ("08:00", "Station I")],
        "Blue Line": [("10:00", "Station J"), ("10:20", "Station K"), ("10:40", "Station L")]
    }
}

print("Transportation Schedule:", schedule)

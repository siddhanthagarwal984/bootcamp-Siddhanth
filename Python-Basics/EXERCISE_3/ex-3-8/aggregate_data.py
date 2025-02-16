from schedule import schedule
from route_schedule import route_schedule

# Combine bus and train data into a single structure
aggregated_data = {
    "All Routes": {**schedule["Bus Routes"], **schedule["Train Lines"]},
    "Individual Schedules": route_schedule
}

print("Aggregated Transportation Data:", aggregated_data)

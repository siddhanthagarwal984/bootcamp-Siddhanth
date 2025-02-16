# Using sets to store unique train and bus stations
train_stations = {
    "Station A", "Station B", "Station C", "Station D", "Station E", "Station F",
    "Station G", "Station H", "Station I", "Station J", "Station K", "Station L"
}
bus_stations = {"Station G", "Station H", "Station M", "Station N", "Station O"}

unique_stations = train_stations.union(bus_stations)
print("Unique Stations:", unique_stations)

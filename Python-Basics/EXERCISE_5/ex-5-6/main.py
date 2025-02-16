from temperature import Temperature

# Valid temperature
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")

# Invalid temperature (raises error)
try:
    temp.celsius = -500
except ValueError as e:
    print(f"Error: {e}")

import requests
import sys

API_KEY = "your_openweathermap_api_key"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city_name):
    """Fetch and display weather information for a given city"""
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather_cli.py <city-name>")
    else:
        fetch_weather(sys.argv[1])

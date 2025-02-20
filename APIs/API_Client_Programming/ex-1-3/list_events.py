import requests

GITHUB_EVENTS_URL = "https://api.github.com/events"

def fetch_public_events():
    """Fetch and display recent public events on GitHub"""
    response = requests.get(GITHUB_EVENTS_URL)

    if response.status_code == 200:
        events = response.json()
        for event in events[:5]:  # Show first 5 events
            print(f"Type: {event['type']} - Repo: {event['repo']['name']}")
    else:
        print("Failed to fetch events:", response.status_code)

if __name__ == "__main__":
    fetch_public_events()

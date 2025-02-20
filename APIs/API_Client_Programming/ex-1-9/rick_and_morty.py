import requests

RICK_AND_MORTY_API = "https://rickandmortyapi.com/api/character"

def fetch_characters():
    """Fetch and display Rick and Morty characters"""
    response = requests.get(RICK_AND_MORTY_API)

    if response.status_code == 200:
        characters = response.json()["results"]
        for char in characters[:5]:  # Show first 5 characters
            print(f"Name: {char['name']} - Species: {char['species']}")
    else:
        print("Failed to fetch characters.")

if __name__ == "__main__":
    fetch_characters()

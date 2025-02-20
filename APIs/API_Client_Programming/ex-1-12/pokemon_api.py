import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon_data(name):
    """Fetch and display Pokémon type information"""
    response = requests.get(POKEAPI_URL + name.lower())

    if response.status_code == 200:
        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        print(f"{name.capitalize()} has types: {', '.join(types)}")
    else:
        print("Pokémon not found.")

if __name__ == "__main__":
    pokemon_name = input("Enter Pokémon name: ")
    fetch_pokemon_data(pokemon_name)

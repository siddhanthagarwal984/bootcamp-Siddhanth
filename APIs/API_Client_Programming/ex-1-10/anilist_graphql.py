import requests

ANILIST_GRAPHQL_URL = "https://graphql.anilist.co"

def fetch_anime_info(title):
    """Fetch and display information about an anime using AniList GraphQL API"""
    query = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
        }
        description
        status
      }
    }
    """
    
    variables = {"search": title}
    
    response = requests.post(ANILIST_GRAPHQL_URL, json={"query": query, "variables": variables})
    
    if response.status_code == 200:
        anime = response.json()["data"]["Media"]
        print(f"Title: {anime['title']['romaji']}")
        print(f"Description: {anime['description']}")
        print(f"Status: {anime['status']}")
    else:
        print("Failed to fetch anime data.")

if __name__ == "__main__":
    anime_title = input("Enter anime title: ")
    fetch_anime_info(anime_title)

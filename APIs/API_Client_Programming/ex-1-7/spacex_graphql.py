import requests

SPACEX_GRAPHQL_URL = "https://spacex-production.up.railway.app/graphql/"

def fetch_latest_launch():
    """Fetch and display the latest SpaceX launch details using GraphQL"""
    query = """
    {
      launchLatest {
        mission_name
        launch_date_utc
        rocket {
          rocket_name
        }
      }
    }
    """

    response = requests.post(SPACEX_GRAPHQL_URL, json={"query": query})

    if response.status_code == 200:
        launch = response.json()["data"]["launchLatest"]
        print(f"Mission: {launch['mission_name']}")
        print(f"Launch Date: {launch['launch_date_utc']}")
        print(f"Rocket: {launch['rocket']['rocket_name']}")
    else:
        print("Failed to fetch launch data:", response.status_code, response.text)

if __name__ == "__main__":
    fetch_latest_launch()

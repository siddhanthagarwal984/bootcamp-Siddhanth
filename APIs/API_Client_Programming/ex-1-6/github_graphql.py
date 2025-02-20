import requests

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
GITHUB_TOKEN = "your_github_token_here"  # Replace with your GitHub token

def fetch_repos(username):
    """Fetch and display a GitHub user's repositories using GraphQL"""
    query = """
    {
      user(login: "%s") {
        repositories(first: 5) {
          nodes {
            name
            description
          }
        }
      }
    }
    """ % username

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(GITHUB_GRAPHQL_URL, json={"query": query}, headers=headers)

    if response.status_code == 200:
        repos = response.json()["data"]["user"]["repositories"]["nodes"]
        for repo in repos:
            print(f"Repo: {repo['name']} - {repo['description']}")
    else:
        print("Failed to fetch repositories:", response.status_code, response.text)

if __name__ == "__main__":
    user = input("Enter GitHub username: ")
    fetch_repos(user)

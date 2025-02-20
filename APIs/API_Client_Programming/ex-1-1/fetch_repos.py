import requests

GITHUB_API_URL = "https://api.github.com/repositories"

def fetch_public_repositories():
    """Fetch and print public repository names from GitHub"""
    response = requests.get(GITHUB_API_URL)
    
    if response.status_code == 200:
        repos = response.json()
        for repo in repos[:10]:  # Limit to first 10 repositories
            print(repo['name'])
    else:
        print("Failed to fetch repositories:", response.status_code)

if __name__ == "__main__":
    fetch_public_repositories()

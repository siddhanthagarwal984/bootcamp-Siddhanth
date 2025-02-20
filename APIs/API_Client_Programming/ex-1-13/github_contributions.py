import requests

GITHUB_USER_CONTRIBUTIONS_URL = "https://github.com/{}"

def fetch_contributions(username):
    """Fetch and display GitHub user contributions"""
    url = GITHUB_USER_CONTRIBUTIONS_URL.format(username)
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Contributions data for {username} is available at: {url}")
    else:
        print("Failed to fetch contributions.")

if __name__ == "__main__":
    user = input("Enter GitHub username: ")
    fetch_contributions(user)

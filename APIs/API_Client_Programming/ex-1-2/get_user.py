import requests
import sys

def get_github_user(username):
    """Fetch and display GitHub user details"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"Name: {user_data.get('name', 'Not available')}")
        print(f"Public Repositories: {user_data.get('public_repos', 'Not available')}")
    else:
        print("User not found or API limit reached.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_user.py <github-username>")
    else:
        get_github_user(sys.argv[1])

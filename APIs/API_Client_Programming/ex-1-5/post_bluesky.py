import requests

BLUESKY_API_URL = "https://api.bsky.app/v1/post"
ACCESS_TOKEN = "your_access_token_here"  # Replace with your Bluesky API token

def post_bluesky_message(message):
    """Post a message to Bluesky"""
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"text": message}

    response = requests.post(BLUESKY_API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        print("Message posted successfully!")
    else:
        print("Failed to post message:", response.status_code, response.text)

if __name__ == "__main__":
    message = input("Enter your message: ")
    post_bluesky_message(message)

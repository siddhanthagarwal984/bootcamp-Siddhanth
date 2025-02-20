import requests

HACKER_NEWS_API_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
HACKER_NEWS_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_top_posts():
    """Fetch and display the top posts from Hacker News"""
    response = requests.get(HACKER_NEWS_API_TOP_STORIES)

    if response.status_code == 200:
        top_story_ids = response.json()[:5]
        for story_id in top_story_ids:
            story = requests.get(HACKER_NEWS_ITEM_URL.format(story_id)).json()
            print(f"Title: {story['title']} - URL: {story.get('url', 'No URL')}")
    else:
        print("Failed to fetch top stories.")

if __name__ == "__main__":
    fetch_top_posts()

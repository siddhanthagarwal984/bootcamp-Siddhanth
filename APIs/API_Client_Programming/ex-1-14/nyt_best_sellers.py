import requests

NYT_API_KEY = "your_api_key_here"
NYT_BEST_SELLERS_URL = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={NYT_API_KEY}"

def fetch_best_sellers():
    """Fetch and display NYT Best Sellers"""
    response = requests.get(NYT_BEST_SELLERS_URL)

    if response.status_code == 200:
        books = response.json()["results"]["books"]
        for book in books[:5]:  # Display top 5 books
            print(f"Title: {book['title']} - Author: {book['author']}")
    else:
        print("Failed to fetch best sellers.")

if __name__ == "__main__":
    fetch_best_sellers()

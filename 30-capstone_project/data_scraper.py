import requests
from bs4 import BeautifulSoup

# BBC News RSS Feed
NEWS_FEED_URL = "http://feeds.bbci.co.uk/news/rss.xml"


def scrape_news():
    try:
        response = requests.get(NEWS_FEED_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        soup = BeautifulSoup(response.text, "xml")
        articles = soup.find_all("item")  # Extract all news items

        # Extract first 5 news headlines
        news_headlines = [article.title.text for article in articles[:5]]

        return news_headlines  # Return a list of news titles

    except requests.exceptions.RequestException as e:
        print(f"News fetching error: {e}")
        return []  # Return an empty list if there's an error

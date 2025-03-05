import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for quote, author in zip(quotes, authors):
        print(f"Quote: {quote.get_text()}")
        print(f"Author: {author.get_text()}")
        print("-" * 40)

else:
    print("Failed to retrieve the page")
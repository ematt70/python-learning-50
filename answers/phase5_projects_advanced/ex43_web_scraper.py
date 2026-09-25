"""
Exercise 43 — Web Scraper (Basic)

Task:
    Fetch a webpage and print all <h2> titles.
"""

import requests
from bs4 import BeautifulSoup

def fetch_h2_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return [h2.get_text() for h2 in soup.find_all("h2")]

def main():
    url = "https://example.com"
    titles = fetch_h2_titles(url)
    for title in titles:
        print("Title:", title)

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup

def get_page(url, output_file="scraped_urls.txt"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tags = soup.find_all("a")

    with open(output_file, "w", encoding='utf-8') as f:
        for tag in tags:
            href = tag.get("href", "")
            if href and href.startswith("https"):
                f.write(href + "\n")


get_page(input("Paste url to scrape "))
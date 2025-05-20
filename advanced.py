import requests
from bs4 import BeautifulSoup



def spider_urls(url, keyword, output_file="scraped_urls.txt"):
    
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    soup =  BeautifulSoup(response.content, 'html.parser')

    tags = soup.find_all("a")

    with open(output_file, "w", encoding='utf-8') as f:
       for tag in tags:
            href = tag.get("href", keyword)
            if href and href.startswith("https"):
                f.write(href + "\n") 










url = input("Enter url to scrape  ")
keyword = input("Enter the keyword")
spider_urls(url, keyword)
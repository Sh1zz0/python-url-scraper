import sys
import requests

def probe(output_file):
    input_urls = sys.stdin.read().splitlines()

    working_urls = []
    bad_urls = []

    for url in input_urls:
        url = url.strip()
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                working_urls.append(url)
            else:
                bad_urls.append(url)
        except (requests.exceptions.MissingSchema,
                requests.exceptions.ConnectionError,
                requests.exceptions.InvalidURL,
                requests.exceptions.Timeout):
            bad_urls.append(url)
        except Exception:
            bad_urls.append(url)

    with open(output_file, 'w') as f:
        f.write('\n'.join(working_urls) + '\n')

urls_file = "scraped_urls.txt"
probe(urls_file)

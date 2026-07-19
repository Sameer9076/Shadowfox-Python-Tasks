import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    # Check agar website properly respond kar rahi hai
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Saare quote blocks ko find karna
        quotes = soup.find_all('div', class_='quote')
        
        print("--- Scraped Quotes & Authors ---")
        for i, quote_block in enumerate(quotes, 1):
            text = quote_block.find('span', class_='text').text
            author = quote_block.find('small', class_='author').text
            print(f"{i}. {text} - By {author}\n")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Scraper run karein
scrape_quotes()
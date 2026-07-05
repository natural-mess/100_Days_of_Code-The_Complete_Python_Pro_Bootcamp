import re
import requests
from bs4 import BeautifulSoup

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/148.0.0.0 Safari/537.36"
    }

class ScrapeData:
    def __init__(self, url):
        _response = requests.get(url=url, headers=HEADER)
        _response.raise_for_status()
        self.soup = BeautifulSoup(_response.text, "html.parser")
        self.list_items = []

    def get_items(self):
        self.list_items = self.soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    def get_links(self):
        item_links = []
        for item in self.list_items:
            link = item.find(name="a", class_="StyledPropertyCardDataArea-anchor")
            item_links.append(link.get("href"))
        return item_links

    def get_prices(self):
        item_prices = []
        for item in self.list_items:
            price = item.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
            if price:
                price_text = price.get_text()
                price_number = re.findall(r"\$\d{1,3}(?:,\d{3})*", price_text)
                item_prices.append(price_number[0])
        return item_prices

    def get_addresses(self):
        item_addresses = []
        for item in self.list_items:
            address = item.find(name="address")
            item_addresses.append(address.get_text().strip().replace(" | ", " "))
        return item_addresses

if __name__ == "__main__":
    data = ScrapeData(url="https://appbrewery.github.io/Zillow-Clone/")
    data.get_items()
    # print(data.get_links())
    # print(data.get_prices())
    print(data.get_addresses())



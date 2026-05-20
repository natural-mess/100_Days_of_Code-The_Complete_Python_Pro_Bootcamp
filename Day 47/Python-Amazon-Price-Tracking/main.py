import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"

# Hints: https://httpbin.org/headers
# https://myhttpheader.com/
HEADER = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "br,gzip",
    "Priority": "u=0, i", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
}

response = requests.get(url=URL, headers=HEADER)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
price = soup.select(".aok-offscreen")
# print(price[1].get_text())

price_without_currency = price[1].get_text().split()[1]
price_float = float(price_without_currency)
print(price_float)

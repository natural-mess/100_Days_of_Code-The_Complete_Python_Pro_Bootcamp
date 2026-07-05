from scrape_data import ScrapeData
from data_entry import DataEntry

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM = "https://forms.gle/f8pE67gS2bKNBL2J6"

data = ScrapeData(ZILLOW_URL)
data.get_items()
links = data.get_links()
print(links)
addresses = data.get_addresses()
print(addresses)
prices = data.get_prices()
print(prices)

form_driver = DataEntry(GOOGLE_FORM)
form_driver.fill_form(links, prices, addresses)

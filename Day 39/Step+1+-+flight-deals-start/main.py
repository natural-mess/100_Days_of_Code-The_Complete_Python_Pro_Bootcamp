#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

DEPARTURE_CODE = "CDG"

# Cache all requests except from sheety
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# Retrieve data from google sheet
data_manager = DataManager()
sheet_data = data_manager.get_sheety_data()
# pprint(sheet_data)

# Retrieve flight data from SerpAPI
flight_search = FlightSearch()
tomorrow = datetime.today() + timedelta(days=1)
six_months_from_now = datetime.today() + timedelta(days=30*6)
# flight_data = flight_search.get_flights_data(DEPARTURE_CODE, "BER", tomorrow, six_months_from_now)
# Print cheapest flight
# flight_data in FlightSearch is already sorted from lowest flight to highest flight
# pprint(flight_data['other_flights'][0])

# Create an instance of the NotificationManager
notification_manager = NotificationManager()

for destination in sheet_data:
    flight_data = flight_search.get_flights_data(DEPARTURE_CODE, destination['iataCode'], tomorrow, six_months_from_now)
    # pprint(destination)
    if flight_data:
        cheapest_flight = flight_data['other_flights'][0]
        if cheapest_flight and cheapest_flight['price'] < destination['lowestPrice']:
            # pprint(f"Lower price flight found to {destination['city']}!")
            # Update google sheet data
            # pprint(destination['id'])
            data_manager.update_sheety_data(destination['id'], cheapest_flight['price'])

            notification_manager.telegram_bot_sendtext(
                bot_message=f"Low price alert! Only EUR {cheapest_flight['price']} to fly "
                             f"from {DEPARTURE_CODE} to {destination['iataCode']}, "
                             f"on {tomorrow.strftime("%Y-%m-%d")} until {six_months_from_now.strftime("%Y-%m-%d")}."
            )
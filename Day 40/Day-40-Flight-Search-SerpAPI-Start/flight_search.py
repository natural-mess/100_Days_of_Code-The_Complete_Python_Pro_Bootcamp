import os
import requests
import requests_cache
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pprint import pprint

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class FlightSearch:

    def __init__(self):
        self._serp_api_key = os.environ.get("SERP_API_KEY")
        self._serp_endpoint = "https://serpapi.com/search.json"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "EUR",
            "stops": "1" if is_direct==True else "0",
            "api_key": self._serp_api_key,
        }

        response = requests.get(url=self._serp_endpoint, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data

if __name__ == '__main__':
    # Setup requests_cache
    requests_cache.install_cache()
    tomorrow = datetime.today() + timedelta(days=1)
    # print(tomorrow)
    six_months_from_now = datetime.today() + timedelta(days=30*6)
    # print(six_months_from_now)
    test_data = FlightSearch()
    flights = test_data.check_flights("CDG", "BKK", tomorrow, six_months_from_now, is_direct=False)
    pprint(flights)
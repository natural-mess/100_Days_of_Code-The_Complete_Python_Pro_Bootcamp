import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        response = requests.get(url=SERPAPI_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data

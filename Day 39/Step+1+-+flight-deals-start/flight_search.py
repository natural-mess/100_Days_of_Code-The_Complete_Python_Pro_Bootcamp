import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._serp_api_key = os.environ.get("SERP_API_KEY")
        self._serp_endpoint = "https://serpapi.com/search.json"

    def get_flights_data(self, departure, arrival, from_time, to_time):
        flight_parameters = {
            "engine": "google_flights",
            "departure_id": departure,
            "arrival_id": arrival,
            "hl": "en",
            "currency": "EUR",
            "type": "1",
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "sort_by": "2",
            "api_key": self._serp_api_key,
        }

        response = requests.get(url=self._serp_endpoint, params=flight_parameters)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        flight_data = response.json()
        if "error" in flight_data:
            print(f"API error: {flight_data['error']}")
            return None
        return flight_data

if __name__ == '__main__':
    tomorrow = datetime.today() + timedelta(days=1)
    # print(tomorrow)
    six_months_from_now = datetime.today() + timedelta(days=30*6)
    # print(six_months_from_now)
    data = FlightSearch()
    print(data.get_flights_data("CDG", "BER", tomorrow, six_months_from_now))



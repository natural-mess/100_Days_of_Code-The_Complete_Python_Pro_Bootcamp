import os
from dotenv import load_dotenv
import requests

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._sheety_endpoint = os.environ.get("SHEETY_FLIGHT_URL_ENDPOINT")
        self._sheety_header = {"Authorization": f"Bearer {os.environ.get('SHEETY_FLIGHT_BEARER_TOKEN')}"}

    def get_sheety_data(self):
        response = requests.get(url=self._sheety_endpoint, headers=self._sheety_header)
        response.raise_for_status()
        sheety_data = response.json()['flights']
        return sheety_data

    def update_sheety_data(self, id_row, lowest_price):
        sheety_request_body = {
            "flight": {
                "lowestPrice": lowest_price,
            }
        }

        sheety_response = requests.put(url=f"{self._sheety_endpoint}/{id_row}", json=sheety_request_body, headers=self._sheety_header)
        # print(sheety_response.text)
        sheety_response.raise_for_status()

if __name__ == '__main__':
    data = DataManager()
    print(data.get_sheety_data())
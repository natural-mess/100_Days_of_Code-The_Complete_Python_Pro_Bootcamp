import os
import requests
import requests_cache
from dotenv import load_dotenv

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class DataManager:

    def __init__(self):
        self._sheety_endpoint = os.environ.get("SHEETY_FLIGHT_URL_ENDPOINT")
        self._sheety_user_endpoint = os.environ.get("SHEETY_FLIGHT_USERS_URL_ENDPOINT")
        self._sheety_header = {"Authorization": f"Bearer {os.environ.get('SHEETY_FLIGHT_BEARER_TOKEN')}"}

    def get_destination_data(self):
        response = requests.get(url=self._sheety_endpoint, headers=self._sheety_header)
        response.raise_for_status()
        sheety_data = response.json()['flights']
        return sheety_data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        sheety_request_body = {
            "flight": {
                "lowestPrice": new_price,
            }
        }
        sheety_response = requests.put(url=f"{self._sheety_endpoint}/{row_id}", json=sheety_request_body,
                                       headers=self._sheety_header)
        # print(sheety_response.text)
        sheety_response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(url=self._sheety_user_endpoint, headers=self._sheety_header)
        response.raise_for_status()
        sheety_data = response.json()['users']
        email_list = []
        for element in sheety_data:
            email_list.append(element['whatIsYourEmail?'])
        return email_list

if __name__ == '__main__':
    # Setup requests_cache
    requests_cache.install_cache(expire_after=360)
    data = DataManager()
    print(data.get_destination_data())
    print(data.get_customer_emails())

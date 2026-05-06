import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)

APP_ID=os.environ.get("APP_ID")
API_KEY=os.environ.get("API_KEY")

NUTRIENT_URL_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

SHEETY_URL_ENDPOINT = os.environ.get("SHEETY_URL_ENDPOINT")

nutrient_headers = {
    "X-APP-ID": APP_ID,
    "X-APP-KEY": API_KEY,
}

nutrient_request_body = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 70,                  # Optional: Weight in kg (1-500)
    "height_cm": 160,                 # Optional: Height in cm (1-300)
    "age": 30,                        # Optional: Age (1-150)
    "gender": "male"                  # Optional: "male" or "female"
}

nutrient_response = requests.post(url=NUTRIENT_URL_ENDPOINT, json=nutrient_request_body, headers=nutrient_headers)
nutrient_response.raise_for_status()
nutrient_data = nutrient_response.json()['exercises'][0]
# print(nutrient_data)

sheety_request_body = {
    "workout": {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%X"),
        "exercise": nutrient_data['name'].title(),
        "duration": nutrient_data['duration_min'],
        "calories": nutrient_data['nf_calories'],
    }
}

# print(datetime.today().strftime("%d%m%Y"))
# print(datetime.now().strftime("%I:%M:%S"))

sheety_header = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {os.environ.get("SHEETY_BEARER_TOKEN")}"
}

sheety_response = requests.post(url=SHEETY_URL_ENDPOINT, json=sheety_request_body, headers=sheety_header)
sheety_response.raise_for_status()
print(sheety_response.text)



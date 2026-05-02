import requests
import os
from dotenv import load_dotenv

load_dotenv("./.env")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_api_key = os.environ.get("OWM_API_KEY")

telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN_KEY")
telegram_bot_chatID = os.environ.get("TELEGRAM_BOT_CHAT_ID")

def telegram_bot_sendtext(bot_message):
    send_text = "https://api.telegram.org/bot" + telegram_bot_token + "/sendMessage?chat_id=" + telegram_bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    response_tele = requests.get(send_text)
    response_tele.raise_for_status()
    return response_tele.json()

# Paris
# MY_LAT = 48.856613
# MY_LONG = 2.352222

# Rennes was raining
MY_LAT = 48.117268
MY_LONG = -1.677793

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": OWM_api_key,
        "cnt":4,
    }

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
id_list = [i['weather'][0]['id'] for i in weather_data['list'][0:]]
# print(id_list)
if any(id_num < 700 for id_num in id_list):
    msg = telegram_bot_sendtext("It's going to rain today. Remember to bring an ☔")
    print(msg)


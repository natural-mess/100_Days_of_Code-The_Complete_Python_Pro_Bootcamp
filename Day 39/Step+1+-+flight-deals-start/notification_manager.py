import os
from dotenv import load_dotenv
import requests

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._telegram_bot_token_key = os.environ.get("TELEGRAM_PYTHON_TEST_BOT_TOKEN_KEY")
        self._telegram_bot_chatID = os.environ.get("TELEGRAM_BOT_CHAT_ID")

    def telegram_bot_sendtext(self, bot_message):
        send_text = "https://api.telegram.org/bot" + self._telegram_bot_token_key + "/sendMessage?chat_id=" + self._telegram_bot_chatID + "&parse_mode=Markdown&text=" + bot_message
        response_tele = requests.get(send_text)
        response_tele.raise_for_status()
        # print(response_tele.json())

if __name__ == '__main__':
    send_message = NotificationManager()
    send_message.telegram_bot_sendtext("This is a test message!")
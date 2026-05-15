import os
from dotenv import load_dotenv
import requests
import smtplib

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._telegram_bot_token_key = os.environ.get("TELEGRAM_PYTHON_TEST_BOT_TOKEN_KEY")
        self._telegram_bot_chatID = os.environ.get("TELEGRAM_BOT_CHAT_ID")
        self._ethereal_email = os.environ.get("ETHEREAL_EMAIL")
        self._ethereal_password = os.environ.get("ETHEREAL_PASSWORD")
        self._ethereal_host = os.environ.get("ETHEREAL_HOST")

    def telegram_bot_send_text(self, bot_message):
        send_text = ("https://api.telegram.org/bot"
                     + self._telegram_bot_token_key
                     + "/sendMessage?chat_id="
                     + self._telegram_bot_chatID
                     + "&parse_mode=Markdown&text="
                     + bot_message)
        response_tele = requests.get(send_text)
        response_tele.raise_for_status()
        # print(response_tele.json())

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self._ethereal_host, 587) as connection:
            connection.starttls()
            connection.login(self._ethereal_email, self._ethereal_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self._ethereal_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8'),
                )


if __name__ == '__main__':
    send_message = NotificationManager()
    send_message.telegram_bot_send_text("This is a test message!")
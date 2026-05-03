# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

from requests_cache import CachedSession
import os
from dotenv import load_dotenv, find_dotenv
from itertools import islice

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)

# STOCK API Key
STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_STOCK_API_KEY")

# NEWS API Key
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Search for BotFather on Telegram and create a bot
# Use https://api.telegram.org/bot<yourtoken>/getUpdates, with <yourtoken> is bot API token to get bot ID
# If result is empty, go to bot setting and turn of Privacy mode
telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN_KEY")
telegram_bot_chatID = os.environ.get("TELEGRAM_BOT_CHAT_ID")

def get_stock_change():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }

    session = CachedSession()
    stock_data = session.get(url="https://www.alphavantage.co/query", params=stock_params)
    stock_data.raise_for_status()

    daily_data = stock_data.json()["Time Series (Daily)"]
    # print(list(daily_data.items())[:2])

    first_two_daily_data = [data["4. close"] for date, data in list(daily_data.items())[:2]]
    return round(((float(first_two_daily_data[1]) - float(first_two_daily_data[0])) / float(first_two_daily_data[0]))*100, 2)

print(get_stock_change())

def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    session = CachedSession()
    news_data = session.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data.raise_for_status()

    # print(news_data.json()["articles"])

    return news_data.json()["articles"][:3]

print(get_news())

def telegram_bot_sendtext(bot_message):
    send_text = "https://api.telegram.org/bot" + telegram_bot_token + "/sendMessage?chat_id=" + telegram_bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    session = CachedSession()
    response_tele = session.get(send_text)
    response_tele.raise_for_status()
    return response_tele.json()

if get_stock_change() > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

tele_msg = (f"TSLA: {emoji} {abs(get_stock_change())}%\n\n"
            f"Headline: {get_news()[0]['title']}\n"
            f"Brief: {get_news()[0]['description']}\n\n"
            f"Headline: {get_news()[1]['title']}\n"
            f"Brief: {get_news()[1]['description']}\n\n"
            f"Headline: {get_news()[2]['title']}\n"
            f"Brief: {get_news()[2]['description']}")

telegram_bot_sendtext(tele_msg)

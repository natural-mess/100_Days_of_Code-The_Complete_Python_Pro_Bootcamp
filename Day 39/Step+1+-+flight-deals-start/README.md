# Flight Deals Finder

A Python application that monitors flight prices and alerts you when deals are found.

## Description
This application automatically checks for cheap flights from a specified departure airport (default: CDG - Paris Charles de Gaulle) to various destinations stored in a Google Sheet. When a flight price drops below the recorded lowest price, it updates the sheet and sends a notification via Telegram.

The app uses:
* Sheety API to interact with Google Sheets
* SerpAPI (Google Flights) for flight search
* Telegram Bot API for notifications
* Requests Cache for efficient API calls

## Features
* Automated flight price monitoring
* Google Sheets integration for destination management
* Real-time price comparison and updates
* Telegram notifications for price drops
* Request caching to optimize API usage
* Configurable departure airport and date ranges

## Prerequisites
* Python 3.7+
* Google account with Google Sheets
* Telegram account for bot creation
* API keys for Sheety, SerpAPI, and Telegram

## Installation
1. Clone the repository:

```bash
git clone https://github.com/natural-mess/100_Days_of_Code-The_Complete_Python_Pro_Bootcamp.git
cd "100 Days of Code - The Complete Python Pro Bootcamp/Day 39/Step+1+-+flight-deals-start"
```

2. Install dependencies:

```bash
pip install requests python-dotenv requests-cache
```

## Setup
### 1. Google Sheets Setup
* Create a new Google Sheet with columns: `id`, `city`, `iataCode`, `lowestPrice`
* Add your destinations (e.g., Paris, London, etc.)
* Share the sheet with Sheety (visit sheety.co to connect your sheet)

### 2. API Keys and Environment Variables
Create a `.env` file in your project directory (or update your existing one at `.env`):

```
SHEETY_FLIGHT_URL_ENDPOINT=https://api.sheety.co/your_username/your_project/flights
SHEETY_FLIGHT_BEARER_TOKEN=your_sheety_bearer_token
SERPAPI_KEY=your_serpapi_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```
### 3. Telegram Bot Setup
* Message `@BotFather` on Telegram to create a new bot
* Get your bot token and chat ID
* Add your bot to a Telegram channel/group or start a chat with it

## Usage
Run the main script:

```bash
python main.py
```

The application will:
1. Fetch destination data from your Google Sheet
2. Search for flights from CDG to each destination
3. Compare prices with stored lowest prices
4. Update the sheet if a better deal is found
5. Send a Telegram notification with flight details

## Configuration
* Departure Airport: Change `DEPARTURE_CODE` in `main.py`
* Date Range: Modify `tomorrow` and `six_months_from_now` for different search periods
* Caching: Adjust cache settings in the `requests_cache.install_cache()` call

## Project Structure

```
flight-deals-start/
├── main.py                 # Main application script
├── data_manager.py         # Google Sheets/Sheety integration
├── flight_search.py        # Flight search using SerpAPI
├── flight_data.py          # Flight data processing
├── notification_manager.py # Telegram notifications
└── README.md              # This file
```

## API Documentation
* Sheety API
* SerpAPI Google Flights
* Telegram Bot API

## Troubleshooting
* 401 Error: Check your Sheety bearer token
* 400 Error: Verify the row ID format (should be integer row numbers)
* Telegram not sending: Confirm bot token and chat ID
* No flight data: Check SerpAPI key and quota

## License
MIT
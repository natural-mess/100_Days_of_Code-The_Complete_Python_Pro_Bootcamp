# Python Flight Club

This project demonstrates how to search for flight deals using the SerpAPI Google Flights API, read destination and customer data from Sheety, and notify users when a lower flight price is found.

## What this project does

- Reads destination data from a Sheety spreadsheet API.
- Searches for flights from a fixed origin airport (`CDG`) to each destination.
- Uses SerpAPI to fetch flight data for a travel window from tomorrow up to six months from today.
- Compares current prices with stored target prices and sends notifications when a cheaper flight is found.
- Supports Telegram messaging and email notifications via SMTP.

## Key files

- `main.py` — orchestrates the flight search and notification flow.
- `data_manager.py` — loads destination and customer email data from Sheety.
- `flight_search.py` — calls the SerpAPI Google Flights endpoint.
- `flight_data.py` — finds the cheapest flight from returned flight data.
- `notification_manager.py` — sends notifications via Telegram and email.
- `Flight Prices.xlsx` — spreadsheet copy of flight destination data.

## Requirements

- Python 3.8+
- `requests`
- `requests_cache`
- `python-dotenv`

## Environment variables

The project loads sensitive configuration from a `.env` file. The current code uses a hardcoded path:

```python
load_dotenv("D:/API/EnvironmentVariables/.env")
```

To run this project locally, create a `.env` file with these values and update the path if needed.

Example variables:

```env
SHEETY_FLIGHT_URL_ENDPOINT=<your_sheety_flight_endpoint>
SHEETY_FLIGHT_USERS_URL_ENDPOINT=<your_sheety_user_endpoint>
SHEETY_FLIGHT_BEARER_TOKEN=<your_sheety_bearer_token>
SERP_API_KEY=<your_serpapi_key>
TELEGRAM_PYTHON_TEST_BOT_TOKEN_KEY=<your_telegram_bot_token>
TELEGRAM_BOT_CHAT_ID=<your_telegram_chat_id>
ETHEREAL_EMAIL=<your_smtp_email>
ETHEREAL_PASSWORD=<your_smtp_password>
ETHEREAL_HOST=<your_smtp_host>
```

## Setup

1. Clone the repository and change into the project folder:

```bash
cd "Python-Flight-Club"
```

2. Create and activate a Python virtual environment.

3. Install dependencies:

```bash
pip install requests requests_cache python-dotenv
```

4. Create or update the `.env` file with your API endpoints and credentials.

5. Run the project:

```bash
python main.py
```

## Notes

- The default origin airport is set to `CDG` (Paris Charles de Gaulle).
- The Sheety spreadsheet controls destination cities, their IATA codes, and current target prices.
- The code currently has notification email and sheet update calls commented out; you can enable them once you confirm everything is working.
- Use secure environment configuration for API keys and credentials, not hardcoded values.

## Recommended improvements

- Add a local `.env` loader path instead of a hardcoded full path.
- Add a `requirements.txt` file for easier dependency installation.
- Add error handling for missing environment variables.
- Add tests for the flight parsing and notification logic.

## License

MIT

# Rain Alert Telegram Bot

A Python script that checks the weather forecast for a specified location and sends a rain alert notification via Telegram if rain is expected.

## Description

This project uses the OpenWeatherMap API to fetch weather data for the next few hours. If any weather condition indicates rain (weather ID < 700), it sends a message to a Telegram chat reminding you to bring an umbrella.

## Prerequisites

- Python 3.x
- OpenWeatherMap API key (free account at [openweathermap.org](https://openweathermap.org/))
- Telegram Bot Token and Chat ID (create a bot via [BotFather](https://t.me/botfather) and get your chat ID)

## Installation

1. Clone or download this repository.
2. Install the required Python packages:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project directory with your API keys and credentials (see Environment Variables section).

## Environment Variables

Create a `.env` file in the root of the project with the following variables:

```
OWM_API_KEY=your_openweathermap_api_key_here
TELEGRAM_BOT_TOKEN_KEY=your_telegram_bot_token_here
TELEGRAM_BOT_CHAT_ID=your_telegram_chat_id_here
```

## Usage

Run the script:

```
python main.py
```

The script will check the weather forecast for the configured location (currently set to Rennes, France). If rain is expected, it will send a notification to your Telegram chat.

## Configuration

- **Location**: Modify `MY_LAT` and `MY_LONG` in `main.py` to set your desired location.
- **Forecast Hours**: Change the `cnt` parameter in the API request to adjust the number of forecast hours to check (default is 4).

## How It Works

1. Loads environment variables from `.env`.
2. Makes a request to OpenWeatherMap API for weather forecast.
3. Checks weather IDs in the forecast (IDs < 700 indicate precipitation).
4. If rain is detected, sends a Telegram message.

## License

MIT
# Stock News Alert System

A Python application that monitors stock price changes and sends automated news alerts via SMS when significant price movements occur.

## Features

- **Stock Price Monitoring**: Tracks daily stock price changes using Alpha Vantage API
- **Automated Alerts**: Sends SMS notifications when stock price changes by more than 5%
- **News Integration**: Fetches latest news articles related to the company using NewsAPI
- **Caching**: Uses `requests_cache` to reduce API calls and improve performance
- **Environment Variables**: Secure API key management using `.env` file

## Prerequisites

- Python 3.7+
- Alpha Vantage API key (free at [alphavantage.co](https://www.alphavantage.co/support/#api-key))
- NewsAPI key (free at [newsapi.org](https://newsapi.org/register))
- Twilio account for SMS (optional, can use Telegram bot instead)

## Installation

1. Clone or download this repository
2. Install required packages:
   ```bash
   pip install requests requests-cache python-dotenv
   ```

3. Create a `.env` file in the project directory with your API keys:
   ```
   ALPHA_VANTAGE_STOCK_API_KEY=your_alpha_vantage_key_here
   NEWS_API_KEY=your_news_api_key_here
   TWILIO_ACCOUNT_SID=your_twilio_sid_here
   TWILIO_AUTH_TOKEN=your_twilio_token_here
   TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
   YOUR_PHONE_NUMBER=your_personal_phone_number_here
   ```

## Configuration

- **STOCK**: Set the stock symbol you want to monitor (default: "TSLA")
- **COMPANY_NAME**: Set the company name for news search (default: "Tesla Inc")
- **Threshold**: Currently set to alert on 5% price changes (can be modified in code)

## Usage

Run the main script:
```bash
python main.py
```

The application will:
1. Fetch the latest stock data
2. Calculate the percentage change between yesterday and the day before yesterday
3. If the change exceeds 5%, fetch the latest 3 news articles
4. Send an SMS with the price change and news headlines

## API Usage

### Alpha Vantage
- Endpoint: `https://www.alphavantage.co/query`
- Function: `TIME_SERIES_DAILY`
- Returns daily stock prices including open, high, low, close, and volume

### NewsAPI
- Endpoint: `https://newsapi.org/v2/everything`
- Searches for articles based on company name
- Returns the 3 most recent articles

### Twilio (SMS)
- Sends formatted SMS messages with stock change and news
- Message format includes emoji indicators (🔺 for increase, 🔻 for decrease)

## Code Structure

- `main.py`: Main application logic
- `get_stock_change()`: Fetches and calculates stock price percentage change
- `get_news()`: Retrieves latest news articles for the company
- `send_sms()`: Sends SMS notification via Twilio

## Caching

The application uses `requests_cache` with `CachedSession()` to cache API responses. This:
- Reduces API calls during development/testing
- Improves response times
- Helps stay within API rate limits

To force fresh data, you can:
- Use `session.get(url, refresh=True)` for individual requests
- Clear cache with `session.cache.clear()`
- Or use `requests.Session()` instead of `CachedSession()`

## Output Format

When a significant price change is detected, you'll receive an SMS like:
```
TSLA: 🔺2.5%
Headline: [News headline 1]
Brief: [Article description]

Headline: [News headline 2]
Brief: [Article description]
```

## Error Handling

The application includes proper error handling for:
- API request failures
- Missing environment variables
- Invalid JSON responses

## Dependencies

- `requests`: HTTP library for API calls
- `requests-cache`: Caching layer for requests
- `python-dotenv`: Environment variable management
- `twilio`: SMS sending (if using Twilio instead of Telegram)

## License
MIT
# Python Auto Tindog Swiping Bot

This script logs into the Tindog practice app through Facebark and performs automated likes while handling common popup and click-interception issues.

## Features

- Opens the Tindog app in Chrome
- Clicks login and chooses Facebark auth
- Logs in on the Facebark popup window and switches back
- Dismisses location, notification, and cookie dialogs
- Auto-likes profiles in a loop
- Handles popup overlays that block Like clicks
- Retries stale/timeout click actions with a helper function

## Demo

![alt text](demo/Tindog_auto_swiping.gif)

## Project Structure

- `main.py`: main Selenium automation script

## Requirements

- Python 3.10+
- Google Chrome installed
- Selenium package

Install dependency:

```bash
pip install selenium
```

## Configuration

Update credentials and URL at the top of `main.py`:

```python
FACEBARK_EMAIL = "your_email@example.com"
FACEBARK_PASSWORD = "your_password"
TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/..."
```

## How It Works

1. Launches Chrome and opens Tindog URL
2. Clicks Tindog login button
3. Clicks Facebark login option
4. Switches to Facebark popup window
5. Submits Facebark credentials
6. Switches back to Tindog window
7. Dismisses location/notification/cookie prompts
8. Runs like loop and closes match popups when they appear

## Run

From this folder:

```bash
python main.py
```

## Current Behavior Notes

- The like loop is currently capped with `for _ in range(20)` in `hit_like()`.
- The script uses helper methods like `safe_click()` and `close_match_popup_if_present()` to improve reliability on dynamic pages.

## Troubleshooting

### `ElementClickInterceptedException`
A popup is usually covering the Like button.

- Ensure popup-close logic runs before trying Like again
- Keep `close_match_popup_if_present()` in the loop

### `StaleElementReferenceException`
The page re-rendered and Selenium lost the element reference.

- Re-find elements just before clicking
- Keep retry logic in `safe_click()`

### `TimeoutException`
Element was not clickable within wait time.

- Increase timeout in `WebDriverWait`
- Check internet connection and page load speed

## Disclaimer

This project is for learning Selenium automation on a training site.
Use automation responsibly and follow terms of service for any real platform.

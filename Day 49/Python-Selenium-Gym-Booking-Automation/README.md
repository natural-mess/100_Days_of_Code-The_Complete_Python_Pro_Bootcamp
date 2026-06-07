# Python Selenium Gym Booking Automation

Automates class booking for the App Brewery gym demo site using Selenium.

This script:
- Logs in to the gym site
- Finds Tuesday and Thursday classes at 6:00 PM
- Books classes or joins the waitlist
- Verifies results on the "My Bookings" page

## Demo Target
- URL: `https://appbrewery.github.io/gym/`

![alt text](demo/Gym_booking_demo.gif)

## Features
- Retry helper for unstable UI interactions
- Persistent Chrome profile (`chrome_profile`) to preserve browser session data
- Summary and verification output in terminal

## Project Structure
- `main.py` - Main automation script
- `chrome_profile/` - Chrome user data directory used by Selenium

## Requirements
- Python 3.10+
- Google Chrome installed
- pip

Python package:
- `selenium`

## Installation
1. Open this project folder.
2. (Optional but recommended) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install selenium
```

## Configuration
Edit the constants in `main.py`:

```python
ACCOUNT_EMAIL = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
GYM_URL = "https://appbrewery.github.io/gym/"
```

## Usage
Run:

```bash
python main.py
```

What happens:
1. Script opens Chrome using the local `chrome_profile` folder
2. Logs in
3. Checks Tue/Thu 6:00 PM classes
4. Books or joins waitlist
5. Navigates to "My Bookings" and verifies count

## Notes
- The first run may take longer while Selenium configures the browser driver.
- If site HTML changes, selectors in `main.py` may need updates.
- Credentials are currently hard-coded for learning purposes. For production use, prefer environment variables.

## Troubleshooting
- `TimeoutException`:
  - Check internet connection
  - Confirm the demo site is reachable
  - Increase waits if needed
- Browser opens but actions fail:
  - Verify page structure/selectors still match
  - Clear `chrome_profile` if session state is corrupted

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE).

# Python Internet Speed X Complaint Bot

Simple Selenium bot that runs an internet speed test and (optionally) logs in to the 100daysofpython "Y" service (X clone) to post a complaint about slow speeds.

## Features
- Run a Speedtest.net check and capture download/upload speeds.
- Automate login to the project's Y service and submit credentials.

## Requirements
- Python 3.8+
- Google Chrome (matching ChromeDriver version)
- ChromeDriver on your PATH or available to Selenium
- Python packages: `selenium`, `python-dotenv`

Install dependencies:

```bash
pip install selenium python-dotenv
```

## Configuration
1. Create a `.env` file with your credentials (do NOT commit secrets):

```
Y_EMAIL=you@example.com
Y_PASSWORD=yourpassword
```

2. By default the project calls `load_dotenv("D:/API/EnvironmentVariables/.env")` in `main.py`.
   - Either update that path to point at your `.env` file, or set the variables in your environment.

## Usage
From the project folder run:

```bash
python main.py
```

- To only test the speed test flow, uncomment the `bot.get_internet_speed()` line in `main.py`.
- The script opens Chrome and (by default) keeps it open so you can inspect what happened.

## Notes & Troubleshooting
- If elements fail to be found, selectors may have changed. Inspect the page and update selectors in `main.py` (use `By.CSS_SELECTOR` for hyphenated class names).
- Ensure your ChromeDriver version matches your Chrome browser version.
- Consider using `webdriver-manager` to auto-manage ChromeDriver if you prefer.

## Contributing
- This is a small learning project. Feel free to open issues or PRs to improve stability and selector handling.

## License
MIT

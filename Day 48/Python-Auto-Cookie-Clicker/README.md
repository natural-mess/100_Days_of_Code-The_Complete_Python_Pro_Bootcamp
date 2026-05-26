# Python Auto Cookie Clicker

A Selenium bot that plays Cookie Clicker automatically by:

- selecting English language at startup
- clicking the big cookie continuously
- buying the most expensive currently available product every few seconds
- printing a minute-by-minute progress update
- stopping after a fixed runtime and printing cookies per second

## Project Structure

- main.py: automation script

## Requirements

- Python 3.9+
- Google Chrome installed
- ChromeDriver compatible with your Chrome version
- Selenium

## Setup (Anaconda)

1. Create and activate an environment:

```bash
conda create -n cookiebot python=3.11 -y
conda activate cookiebot
```

2. Install dependencies:

```bash
pip install selenium
```

3. Open the project folder in VS Code and make sure this conda environment is selected as interpreter.

## Run

From this folder:

```bash
python main.py
```

The script opens:

https://ozh.github.io/cookieclicker/

It runs for 5 minutes by default, then prints final cookies/second and closes the browser.

## Configuration

You can tune these values in main.py:

- timeout: total bot run duration
- UPGRADE_EVERY: how often to try buying a product
- ONE_MIN: interval for progress logging

Quick examples:

- Run for 10 minutes: change timeout to time.time() + 60 * 10
- Upgrade every 2 seconds: set UPGRADE_EVERY = 2

## How The Bot Works

1. Launches Chrome with Selenium.
2. Loads the Cookie Clicker page.
3. Waits for and clicks EN language selector.
4. Waits for DOM rebuild after language switch.
5. Enters click loop:
   - spam-click big cookie
   - every UPGRADE_EVERY seconds, buy the last enabled product in the store list
   - print progress every minute
6. Exits at timeout and prints cookies/second.

## Common Issues

### Script says Selenium import cannot be resolved in editor

Your editor may be using a different interpreter than your conda environment.

- Select the same conda env in VS Code interpreter picker
- Confirm selenium is installed in that env

### Browser opens then closes immediately

- Check for uncaught runtime errors in terminal output
- Ensure Chrome and ChromeDriver are compatible

### Cookie Clicker UI changed and selectors fail

If element IDs/classes change, update selectors in main.py:

- langSelect-EN
- bigCookie
- .product.unlocked.enabled
- cookiesPerSecond

## Notes

- This script is for learning Selenium automation.
- Website structure updates can require selector updates over time.

## License
MIT

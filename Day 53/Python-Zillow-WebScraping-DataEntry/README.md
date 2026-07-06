# Zillow Web Scraping & Data Entry Automation

This project demonstrates how to combine web scraping and browser automation to collect property information from a sample Zillow-style page and submit it into a Google Form automatically.

## Project Idea

The main goal is to reduce manual data entry. Instead of copying property addresses, prices, and links by hand, the script:

1. Opens a target webpage that contains property listings.
2. Extracts relevant data such as:
   - property address
   - price
   - listing link
3. Opens a Google Form and fills in the extracted values automatically.

This is a practical example of using Python for automation, scraping, and form submission.

![alt text](demo/demo.gif)

## How the Solution Works

### 1. Scraping the listings
The file scrape_data.py uses:

- requests to download the webpage HTML
- BeautifulSoup to parse the page structure
- custom selectors to find listing cards and read their fields

It collects:

- listing links
- prices
- addresses

### 2. Filling the form
The file data_entry.py uses Selenium to:

- open a browser session
- navigate to the Google Form URL
- locate the form fields
- enter the scraped data
- submit the form
- continue to the next entry

### 3. Orchestrating everything
The file main.py connects the two parts:

- it creates a scraper object
- extracts the data
- passes it into the form-filling automation

## Project Structure

- main.py: main script that runs the whole workflow
- scrape_data.py: handles fetching and extracting listing data
- data_entry.py: handles browser automation and form submission

## Requirements

Make sure you have:

- Python 3.8 or newer
- Google Chrome installed
- ChromeDriver available on your system PATH

Install the required Python packages:

```bash
pip install requests beautifulsoup4 selenium
```

## How to Run It

1. Open a terminal in this project folder.
2. Make sure your Python environment is activated.
3. Install the required packages if needed.
4. Run the main script:

```bash
python main.py
```

## Important Notes

- The scraper is built for the specific demo Zillow-style page used in the project.
- If the website layout changes, the CSS or class selectors may need to be updated.
- The form automation depends on the Google Form structure staying compatible with the selectors used in the code.
- ChromeDriver must be installed and accessible for Selenium to work.

## What You Learn From This Project

This project teaches:

- how to scrape structured data from HTML pages
- how to use BeautifulSoup for parsing
- how to automate browsers with Selenium
- how to connect data extraction and data entry into a single workflow

## Disclaimer

Please use web scraping and automation responsibly and in accordance with the website’s terms of service.

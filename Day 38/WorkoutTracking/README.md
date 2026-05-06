# Workout Tracking App

This is a Python application that tracks your workouts by taking input of exercises performed, querying the Nutritionix API for exercise data, and logging it to a Google Sheet via the Sheety API.

## Features

- Input exercises in natural language (e.g., "I ran 5 miles")
- Automatic calculation of calories burned and exercise duration
- Logs workout data to a Google Sheet for easy tracking

## Prerequisites

- Python 3.x
- API keys from Nutritionix and Sheety

## Setup

1. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Get API Keys**:
   - Sign up for a free account at [Nutritionix API](https://app.100daysofpython.dev/services/nutrition/docs)
   - Create a Sheety account at [Sheety](https://sheety.co/)
   - Set up a Google Sheet and connect it to Sheety to get your endpoint URL and bearer token

3. **Environment Variables**:
   Create a `.env` file in the project directory with the following content:
   ```
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   SHEETY_URL_ENDPOINT=https://api.sheety.co/your_project_id/your_sheet_name/workouts
   SHEETY_BEARER_TOKEN=your_sheety_bearer_token
   ```

## How to Run

1. Ensure your `.env` file is set up with valid API keys.
2. Run the application:
   ```
   python main.py
   ```
3. Follow the prompt to enter the exercises you performed (e.g., "I ran for 30 minutes and lifted weights").

The app will query the Nutritionix API, extract exercise data, and post it to your Google Sheet.

## Notes

- This project is part of Day 38 of the "100 Days of Code - The Complete Python Pro Bootcamp" course.
- The app uses default values for weight (70kg), height (160cm), age (30), and gender (male). You can modify these in the code if needed.
- Ensure your Google Sheet has columns for date, time, exercise, duration, and calories.

## Troubleshooting

- If you get API errors, verify your keys and endpoints in the `.env` file.
- Check that your Sheety endpoint matches your Google Sheet structure.
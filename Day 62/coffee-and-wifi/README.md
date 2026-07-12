# Coffee & WiFi ☕💪🔌

A Flask web application to discover and share the best coffee shops with ratings for coffee quality, WiFi strength, and power socket availability.

## Features

- **Browse Cafes**: View all registered cafes with their ratings and details
- **Add New Cafes**: Submit new coffee shops with complete information
- **Emoji Ratings**: Visual ratings using emojis for easy understanding:
  - ☕ Coffee quality (1-5 cups)
  - 💪 WiFi strength (0-5 bars)
  - 🔌 Power sockets (1-5 outlets)
- **Form Validation**: Server-side validation ensures data quality
- **Data Persistence**: All cafe data stored in CSV format

## Technologies Used

- **Flask** - Web framework
- **Flask-WTF** - Form handling with CSRF protection
- **Flask-Bootstrap5** - Responsive UI styling
- **WTForms** - Form validation
- **CSV** - Data storage

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Ensure `cafe-data.csv` exists in the project directory

## Running the Application

```bash
python main.py
```

Then open your browser and navigate to `http://localhost:5000`

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/add` | GET, POST | Add new cafe form and submission |
| `/cafes` | GET | View all cafes |

## Project Structure

```
coffee-and-wifi/
├── main.py                 # Flask app and routes
├── requirements.txt        # Dependencies
├── cafe-data.csv          # Cafe database
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── add.html           # Add cafe form
│   └── cafes.html         # Cafes listing
└── README.md              # This file
```

## How It Works

### Adding a Cafe

1. Navigate to `/add`
2. Fill out the form with:
   - Cafe name
   - Google Maps location URL
   - Opening and closing times
   - Select ratings for coffee, WiFi, and power sockets
3. Submit the form
4. Validation checks if all fields are properly filled
5. If valid, data is written to `cafe-data.csv` and new row starts on a new line
6. User is redirected to `/cafes` to see updated list

### Data Format

The emoji values are stored in the CSV for readability:
- Coffee/WiFi/Power ratings stored as emoji strings (☕☕, 💪💪💪, etc.)
- Makes the raw CSV file human-readable

## Form Validation

- **Cafe Name**: Required text field
- **Location URL**: Required URL field with format validation
- **Opening/Closing Time**: Required text fields (format: "8AM", "5:30PM")
- **Coffee Rating**: Required selection (1-5)
- **WiFi Rating**: Required selection (0-5)
- **Power Sockets**: Required selection (1-5)

All validation happens on the server-side using `validate_on_submit()`.

## Key Concepts Used

- **`validate_on_submit()`**: Combines POST request check + form validation
- **`methods=['GET', 'POST']`**: Allows both displaying and submitting forms
- **`csv.writer`**: Properly formats CSV rows with automatic newlines
- **`dict().get()`**: Converts SelectField choices to display their emoji values
- **Jinja2 Templates**: Dynamic HTML rendering with Flask

## Development Notes

- The app requires a `SECRET_KEY` for session management
- CSRF token validation is automatic with Flask-WTF
- Browser-side validation is disabled (`novalidate=True`) in favor of server-side validation
- Emoji support requires UTF-8 encoding

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication
- Rate limiting
- Search and filter capabilities
- Google Maps integration
- Star ratings or review comments

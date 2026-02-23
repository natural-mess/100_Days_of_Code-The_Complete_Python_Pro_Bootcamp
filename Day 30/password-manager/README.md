# Password Manager

A simple yet functional password manager built with Python's Tkinter GUI framework. Securely store, generate, and retrieve passwords for your online accounts.

## Features

- **Generate Secure Passwords**: Automatically creates strong, randomized passwords containing letters (both cases), numbers, and symbols
- **Save Passwords**: Store website credentials (website, email/username, and password) securely in a JSON file
- **Search Passwords**: Quickly retrieve stored passwords for any website
- **Auto-copy to Clipboard**: Generated passwords are automatically copied to your clipboard for easy use
- **Update Existing Entries**: Overwrite passwords for websites you already have saved
- **User-friendly GUI**: Clean, intuitive interface built with Tkinter

## Requirements

- Python 3.x
- `pyperclip` library (for clipboard functionality)

## Installation

1. Install the required dependency:
```bash
pip install pyperclip
```

2. Ensure you have the `logo.png` file in the same directory as `main.py`

## Usage

1. Run the application:
```bash
python main.py
```

2. **Generate a Password**:
   - Click the "Generate Password" button to create a new secure password
   - The password will automatically appear in the password field and be copied to your clipboard

3. **Save a Password**:
   - Enter the website name (e.g., "Gmail", "Twitter")
   - Enter your email or username
   - Enter the password (or generate one)
   - Click "Add" to save
   - Confirm the details in the dialog box

4. **Search for a Password**:
   - Enter the website name
   - Click "Search" to retrieve your saved credentials
   - A dialog will display the stored email and password

## Data Storage

Passwords are stored locally in a `data.json` file in JSON format:

```json
{
    "Website Name": {
        "username": "your_email@example.com",
        "password": "GeneratedPassword123!#"
    }
}
```

## Security Notes

⚠️ **Important**: This is a learning project. For production use, consider:
- Encrypting the data.json file
- Using proper credential management systems
- Never commit data.json to version control
- Implementing master password protection
- Using industry-standard password managers for sensitive production use

## Project Structure

```
password-manager/
├── main.py          # Main application file
├── data.json        # Stores saved passwords (created on first save)
├── logo.png         # Application icon
└── README.md        # This file
```

## How It Works

1. **Password Generation**: Uses random selection of characters from predefined sets of letters, numbers, and symbols, then shuffles them for randomness

2. **Password Storage**: Uses Python's `json` module to store credentials in a structured format, allowing for easy updates and retrieval

3. **File Handling**: Implements try-except-else-finally blocks to handle file operations gracefully (file not found, JSON decode errors, etc.)

4. **GUI Components**: Tkinter widgets organized in a grid layout for clean presentation

## Future Enhancement Ideas

- Add master password protection
- Encrypt stored passwords
- Export passwords to CSV
- Password strength indicator
- Dark mode theme
- Search filter/category options
- Delete password entries

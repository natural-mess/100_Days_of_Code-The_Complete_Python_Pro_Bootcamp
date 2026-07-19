# Cafe & Wifi API

A simple Flask REST API for discovering and managing cafes with wifi, power sockets, and work-friendly amenities.

## Features

- Get a random cafe
- List all cafes
- Search cafes by location
- Add a new cafe
- Update cafe coffee price
- Delete a cafe (protected by API key)

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite

## Project Structure

- `main.py` - Flask app, database model, and API routes
- `templates/index.html` - Landing page
- `requirements.txt` - Python dependencies
- `instance/cafes.db` - SQLite database file (created at runtime)

## Setup

1. Clone or download this project.
2. Open a terminal in the project folder.
3. (Optional but recommended) Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
python main.py
```

The server starts at:

- `http://127.0.0.1:5000`

## API Documentation

Public Postman docs:

- https://documenter.getpostman.com/view/56738718/2sBY4PNzbv

## Endpoints

### `GET /`

Returns the landing page.

### `GET /random`

Returns one random cafe.

Example response:

```json
{
    "cafe": {
        "can_take_calls": true,
        "coffee_price": "£2.30",
        "has_sockets": true,
        "has_toilet": true,
        "has_wifi": true,
        "id": 9,
        "img_url": "https://lh3.googleusercontent.com/p/AF1QipMrdTyRRozGBltwxAseQ4QeuNhbED6meQXlCPsx=s0",
        "location": "London Bridge",
        "map_url": "https://goo.gl/maps/LU1imQzBCRLFBxKUA",
        "name": "The Southwark Cathedral Cafe",
        "seats": "20-30"
    }
}
```

### `GET /all`

Returns all cafes.

### `GET /search?loc=<location>`

Returns cafes matching the given location.

### `POST /add`

Adds a new cafe using form data.

Expected form fields:

- `name`
- `map_url`
- `img_url`
- `loc`
- `seats`
- `sockets`
- `toilet`
- `wifi`
- `calls`
- `coffee_price`

### `PATCH /update-price/<cafe_id>?new_price=<price>`

Updates a cafe coffee price.

### `DELETE /report-closed/<cafe_id>?api_key=<key>`

Deletes a cafe by id.

- API key currently set in code as `TopSecretAPIKey`.
- Also accepts `api-key` for compatibility.

## Notes

- Database tables are created automatically on startup.
- For production usage, move secrets (like API keys) to environment variables.

## License

MIT

# CineRank — Personal Top Movies Tracker

A Flask web app that lets you build and manage your personal ranked movie list, powered by live data from [The Movie Database (TMDB)](https://www.themoviedb.org/) API.

## Features

- **Search & Add** — Search any movie title and pull its details (poster, year, description) directly from TMDB.
- **Rate & Review** — Add your personal rating (out of 10) and a short review for each movie.
- **Auto-Ranking** — Movies are automatically ranked from lowest to highest rating each time the home page loads.
- **Edit** — Update your rating or review for any movie at any time.
- **Delete** — Remove a movie from your list.

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | Flask 2.3 |
| Database ORM | Flask-SQLAlchemy 3.1 + SQLAlchemy 2.0 |
| Database | SQLite |
| Forms | Flask-WTF + WTForms |
| Styling | Bootstrap 5 (Bootstrap-Flask) |
| External API | TMDB REST API v3 |

## Project Structure

```
├── main.py               # App factory, models, routes
├── requirements.txt      # Python dependencies
├── templates/
│   ├── base.html         # Shared layout
│   ├── index.html        # Home — ranked movie list
│   ├── add.html          # Search form
│   ├── select.html       # Search results picker
│   └── edit.html         # Rate & review form
├── static/               # CSS / images
└── instance/
    └── movies.db         # SQLite database (auto-created)
```

## Setup

### 1. Clone & install dependencies

```bash
# Windows
python -m pip install -r requirements.txt

# macOS / Linux
pip3 install -r requirements.txt
```

### 2. Get a TMDB API key

1. Create a free account at [themoviedb.org](https://www.themoviedb.org/).
2. Go to **Settings → API** and generate an API Read Access Token (Bearer token).

### 3. Configure the environment variable

Create a `.env` file (or add to your existing one) with:

```env
THE_MOVIE_DB_HEADER=your_tmdb_read_access_token_here
```

Update the path in `main.py` if your `.env` file is not at `D:/API/EnvironmentVariables/.env`:

```python
load_dotenv("path/to/your/.env")
```

### 4. Run the app

```bash
python main.py
```

Open `http://127.0.0.1:5000` in your browser.

## Usage

1. Click **Add Movie** and type a title to search TMDB.
2. Pick the correct movie from the results.
3. You'll be redirected to the **Edit** page — give it a rating and review.
4. Back on the home page your movies are ranked automatically by rating.
5. Use the **Edit** or **Delete** buttons on any card to manage your list.

## Notes

- The SQLite database is created automatically at `instance/movies.db` on first run.
- If you change the database schema (e.g. column nullability), delete `instance/movies.db` and restart the app so it is recreated with the updated schema. `db.create_all()` does **not** alter existing tables.

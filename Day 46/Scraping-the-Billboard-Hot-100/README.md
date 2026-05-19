# Billboard Hot 100 to YouTube Music Playlist

A Python script that scrapes the Billboard Hot 100 chart for a given date and automatically creates a YouTube Music playlist with those songs.

## How It Works

1. Prompts you for a date (format: `YYYY-MM-DD`)
2. Scrapes the Billboard Hot 100 chart for that date
3. Checks if a playlist with that name already exists in your YouTube Music library
   - If it exists, reuses it
   - If not, creates a new private playlist
4. Searches YouTube Music for each song and adds it to the playlist

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `ytmusicapi`

Install dependencies:

```bash
pip install requests beautifulsoup4 ytmusicapi
```

## Setup

### YouTube Music Authentication

This project uses `ytmusicapi` with browser authentication. You need a `browser.json` file with your credentials.

To generate it, run:

```bash
ytmusicapi browser
```

Follow the instructions to paste your request headers from your browser. This will create the `browser.json` file.

## Usage

```bash
python main.py
```

When prompted, enter a date like `2026-05-16` to create a playlist with that week's Billboard Hot 100 songs.

## Example Output

```
Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: 2026-05-16
Created new playlist: PLxxxxxxxxxxxxxxx
Added: Song Title 1
Added: Song Title 2
Skipped Some Song | Reason: ...
```

Running again with the same date will reuse the existing playlist instead of creating a duplicate.

## License
MIT
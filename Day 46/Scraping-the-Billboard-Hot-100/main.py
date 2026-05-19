import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

URL = "https://www.billboard.com/charts/hot-100"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/148.0.0.0 Safari/537.36"
    }

date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"{URL}/{date}", headers=header)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.css.select('li > .c-title')

top_100_song_list = [song.get_text().strip() for song in song_titles]

# test date : 2026-05-16
# print(top_100_song_list)

# Verify authentication works
yt = YTMusic("browser.json")
# playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")
# print(playlists)
# current_playlist_titles = [title['title'] for title in playlists]
# print(current_playlist_titles)

# Create new yt music playlist or reuse existing one
new_playlist_name = f"{date} Billboard 100"

existing_playlists = yt.get_library_playlists()
new_playlist_id = None
for p in existing_playlists:
    if p['title'] == new_playlist_name:
        new_playlist_id = p['playlistId']
        break

if new_playlist_id is None:
    new_playlist_id = yt.create_playlist(
        new_playlist_name,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print(f"Created new playlist: {new_playlist_id}")
else:
    print(f"Using existing playlist: {new_playlist_id}")
# print(f"Playlist with id {new_playlist_id} created.")

# For testing
# top_100_song_list = ['Be Her', 'Man I need']

for song in top_100_song_list:
    try:
        search_result = yt.search(song, filter="songs", limit = 1)
        # print(search_result[0]["videoId"])
        add_to_playlist = yt.add_playlist_items(
                playlistId = new_playlist_id,
                videoIds = [search_result[0]["videoId"]],
                duplicates = False
            )
        # print(add_to_playlist)
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped {song} | Reason: {e}")


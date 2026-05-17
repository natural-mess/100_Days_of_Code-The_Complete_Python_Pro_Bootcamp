import requests
from bs4 import BeautifulSoup

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
print(top_100_song_list)

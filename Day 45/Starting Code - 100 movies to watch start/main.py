import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

empire_online_webpage = response.text
soup = BeautifulSoup(empire_online_webpage, "html.parser")
# print(soup.prettify())

titles = soup.find_all(name="h3", class_="title")

titles_sorted = reversed(titles)

# for title in titles_sorted:
#     print(title.get_text())

with open("movies.txt", "w", encoding="utf-8") as f:
    for title in titles_sorted:
        f.write(f"{title.get_text()}\n")

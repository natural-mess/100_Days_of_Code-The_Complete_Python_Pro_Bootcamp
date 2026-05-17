from os import name

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)

    link = article_tag.select('a')[0].get('href')
    article_links.append(link)

    # article_upvote = soup.find(name="span", class_="score").get_text()
    # print(article_upvote)

# article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

article_upvotes = []
sub_text = soup.find_all(name="td", class_="subtext")
for text in sub_text:
    score = text.find(name="span", class_="score")
    # handle the case in which an article doesn't have score
    if text.find(name="span", class_="score"):
        article_upvotes.append(int(score.get_text().split()[0]))
    else:
        article_upvotes.append(0)

# print(int(article_upvotes[0].split()[0]))

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(max(article_upvotes))

highest_score_index = article_upvotes.index(max(article_upvotes))
print(highest_score_index)
print(article_texts[highest_score_index])
print(article_links[highest_score_index])

# print(len(article_upvotes))
# print(len(article_texts))
# print(len(article_links))



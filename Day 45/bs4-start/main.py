from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

# print(soup.find_all(name='a'))

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# company_url = soup.select_one(selector="#name")
# print(company_url)

print(soup.select(".heading"))


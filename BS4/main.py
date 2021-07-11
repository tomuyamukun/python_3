from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    pass

heading = soup.find(name="h1", id="name")

section_heading = soup.find(name="h3", attrs={'class': "heading"})
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

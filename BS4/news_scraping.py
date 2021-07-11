from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)

web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

articles = soup.find_all("a", attrs={"class": "storylink"})
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)


article_upvotes = [
    int(score.getText().split()[0]) for score in soup.find_all(
        "span", attrs={
            "class": "score"})]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
print(article_upvotes)
# print(int(article_upvotes[0].split(" ")[0]))

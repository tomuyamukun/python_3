# 現状動的に生成され、スクレイピング不可
import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')


movie_title_tags = soup.find_all("h3", attrs={"class": "jsx-4245974604"})
movie_titles = [movie.getText() for movie in movie_title_tags]

movies = movie_titles[::-1]

with open("movies.txt", mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")

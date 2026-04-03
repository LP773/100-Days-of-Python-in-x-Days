from bs4 import BeautifulSoup
import requests

destination_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(destination_url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

scrapped_titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.text for title in scrapped_titles]
movie_titles.reverse()

with open("movies.txt", 'w') as file:
    for item in movie_titles:
        file.write(item + "\n")


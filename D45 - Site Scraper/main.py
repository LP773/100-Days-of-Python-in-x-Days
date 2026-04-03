from bs4 import BeautifulSoup
import requests

y_combinator_url = "https://news.ycombinator.com/news"
response = requests.get(y_combinator_url)
yc = response.text

soup = BeautifulSoup(yc, "html.parser")
title_lines = soup.find_all(name='span', class_='titleline')
subline_lines = soup.find_all(name='span', class_="score")

titles = [title.text for title in title_lines]
links = [title.a['href'] for title in title_lines]
scores = [int(score.text.split()[0]) for score in subline_lines]

for item in range(len(titles) - 1):
    print(titles[item])
    print(links[item])
    print(scores[item])
    print("")

highest_score = max(scores)
index = scores.index(highest_score)
print("====================================")
print("THE HIGHEST SCORE IS", highest_score)
print(titles[index])
print(links[index])
print(scores[index])


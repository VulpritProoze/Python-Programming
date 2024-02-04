'''
Exercise 17

Use the BeautifulSoup and requests Python packages to print out 
a list of all the article titles on the New York Times homepage.
'''

import requests
import re
from bs4 import BeautifulSoup


url = "https://www.nytimes.com"
response = requests.get(url)
html_response = response.text

html_soup = BeautifulSoup(html_response, "html.parser")

'''
nav_to_heading = html_soup.find_all(class_="story-heading")
article_titles = []
for i,story_heading in html_soup.find_all(class_="story-heading"):
    article_titles[i] = story_heading
for titles in article_titles:
    print(titles.string)'''   
'''
This stupid ahh code does not work. I have looked through the html of nwtimes
and found no "story-heading" class at all. I didn't even find any ids
that would make the titles unique and therefore easy to pick out.
I don't think this can be solved with my little brain

Best I can do is switch into a different news website?
'''

nav_to_storywrapper = html_soup.find_all("section", class_="story-wrapper")

article_titles = []
ignore_tags = ["Spelling Bee", "Connections", "Letter Boxed", "The Crossword", "Wordle", "Connections Companion"]
# ignore_tags not used

for paragraph in nav_to_storywrapper:
    article_titles.append(paragraph.find("p", class_="indicate-hover"))      

article_titles = list( set( article_titles))
article_titles = [title.string for title in article_titles if title is not None]

# filter out unneeded items
temp_list = article_titles
for i, title in enumerate(article_titles):
    for tag in ignore_tags:
        if title == tag:
            temp_list.remove(title)

for i, titles in enumerate(article_titles):
    if titles != None:
        print(f"{i+1}. {titles}")
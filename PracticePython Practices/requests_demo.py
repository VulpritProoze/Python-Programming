import requests
from bs4 import BeautifulSoup

url = "http://github.com"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="lxml")
title = soup.find_all(["p"])

title_strings = []

for e in title:
    title_strings.append(e.string)

print(*title_strings, sep="\n")


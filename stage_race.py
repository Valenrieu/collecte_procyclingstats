#!/bin/python3

from requests import get
from bs4 import BeautifulSoup

# Renvoie un tuple qui contient le nombre d'etapes et un tableau
# de liens vers les etapes

def get_stages_links(url):
    table = None
    count = 0
    links = []
    req = get(url)
    page = BeautifulSoup(req.text, "html.parser")
    h3 = page.find_all("h3")

    for title in h3:
        if title.string=="Stages":
            table = title.parent.find("table").find("tbody")
            break

    for line in table.find_all("tr"):
        count += 1
        links.append(url+f"/stage-{str(count)}")

    return count, links

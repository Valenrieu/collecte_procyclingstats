from requests import get
from bs4 import BeautifulSoup

class RaceCancelledError(Exception):
    def __init__(self, message=""):
        super().__init__(message)

# Renvoie les liens des etapes d'une course a etapes

def get_stages_links(url):
    if url[-2::]!="gc":
        raise RaceCancelledError()

    table = None
    count = 0
    links = []
    url = url[:-2]
    req = get(url)
    page = BeautifulSoup(req.text, "html.parser")
    h3 = page.find_all("h3")

    for title in h3:
        if title.string=="Stages":
            table = title.parent.find("table").find("tbody")
            break

    for line in table.find_all("tr"):
        if line.find_all("td")[2].string=="Restday":
            continue

        if "Prologue" in line.find_all("td")[2].string:
            text = line.find("a").get("href")
            if "tour-de-romandie" in text:
                links.append(url+f"stage-0")
            
            else:
                links.append(url+"prologue")
            
            continue

        count += 1
        links.append(url+f"stage-{str(count)}")

    return links

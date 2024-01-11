from requests import get
from bs4 import BeautifulSoup

class RaceCancelledError(Exception):
    def __init(self, message=""):
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
        count += 1
        links.append(url+f"stage-{str(count)}")

    return links
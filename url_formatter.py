from urllib.parse import urlencode
from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://www.procyclingstats.com"

# Attributs statiques pour les differentes categories
# Equivalent d'une enum Java, a utiliser pour la fonction get_url
# via l'argument uci_ciruit.

class UciCircuit:
    WORLD_TOUR = 1
    WORLD_CHAMPIONSHIPS = 2
    MEN_JUNIOR = 15
    WOMEN_ELITE = 16
    WOMEN_JUNIOR = 17
    NATIONAL_CHAMPIONSHIPS = 23
    WOMEN_WORLD_TOUR = 24
    EUROPE_TOUR = 13
    AFRICA_TOUR = 11
    ASIA_TOUR = 12
    OCEANIA_TOUR = 14
    AMERICA_TOUR = 18
    UCI_PRO_SERIES = 26
    OLYMPIC_GAMES = 3
    NATIONS_CUP = 21

# Formater une URL

def get_url(year=None, uci_circuit=None, classification=None):
    url = BASE_URL+"/races.php?"
    params = {"year":str(year), "circuit":str(uci_circuit),
              "class":classification, "filter":"Filter"}
    # Supprimer les None
    params = dict((k, v) for k, v in params.items() if v is not None)
    return url+urlencode(params)

def get_races_links(url):
    links = []
    req = get(url)
    page = BeautifulSoup(req.text, "html.parser")
    table = page.find("table").tbody

    for line in table.find_all("tr"):
        link = line.find("a")
        links.append(BASE_URL+"/"+link.get("href"))

    return links

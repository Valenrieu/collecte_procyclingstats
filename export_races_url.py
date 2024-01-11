from url_formatter import UciCircuit, get_url, get_races_links
from stage_race import RaceCancelledError, get_stages_links

CIRCUITS = [UciCircuit.WORLD_TOUR, UciCircuit.WORLD_CHAMPIONSHIPS,
            UciCircuit.EUROPE_TOUR, UciCircuit.UCI_PRO_SERIES,
            UciCircuit.NATIONAL_CHAMPIONSHIPS]

CLASSIFICATION = {UciCircuit.WORLD_TOUR:["1.UWT", "2.UWT"],
                  UciCircuit.EUROPE_TOUR:["1.1", "2.1"],
                  UciCircuit.UCI_PRO_SERIES:["1.Pro", "2.Pro"]}

YEAR = 2023
FILE_PATH = "races_url.txt"

open(FILE_PATH, "w").close() # Vider le fichier

def write_url(url):
    with open(FILE_PATH, "a") as file:
        file.write(url+"\n")

def export_stages_race():
    urls = [get_url(YEAR, CIRCUITS[0], CLASSIFICATION.get(CIRCUITS[0])[1]),
            get_url(YEAR, CIRCUITS[2], CLASSIFICATION.get(CIRCUITS[2])[1]),
            get_url(YEAR, CIRCUITS[3], CLASSIFICATION.get(CIRCUITS[3])[1])]

    for url in urls:
        try:
            for link in get_races_links(url):
                write_url(link)

                for link1 in get_stages_links(link):
                    write_url(link1)

        except RaceCancelledError:
            continue

# Exporte les liens des courses de championnat, je filtre car
# dans la categorie championnat, les junior, femmes et les contre
# la montre par equipes sont melanges avec les courses homme.

def export_championships_races():
    urls = [get_url(YEAR, CIRCUITS[1]),
            get_url(YEAR, CIRCUITS[4])]

    for url in urls:
        for link in get_races_links(url):
            if ("we" in link or "mu" in link or "wj" in link or "mj" in link or
                "ttt" in link or "wu" in link or "u23" in link or "women" in link or "junior" in link): 
                continue

            write_url(link)

def export_one_day_races():
    urls = [get_url(YEAR, CIRCUITS[0], CLASSIFICATION.get(CIRCUITS[0])[0]),
            get_url(YEAR, CIRCUITS[2], CLASSIFICATION.get(CIRCUITS[2])[0]),
            get_url(YEAR, CIRCUITS[3], CLASSIFICATION.get(CIRCUITS[3])[0])]

    for url in urls:
        for link in get_races_links(url):
            write_url(link)

def export_urls():
    export_stages_race()
    export_championships_races()
    export_one_day_races()

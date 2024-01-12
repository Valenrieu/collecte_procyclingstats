#!/bin/python3

from requests import get
from bs4 import BeautifulSoup
import pandas as pd

from stage_race import RaceCancelledError

def find_race_info(html):
    res = [html.find("h1").string]

    try:
        res.append(html.find_all("font")[3].string[1:-1])

    except IndexError:
        res.append(html.find_all("font")[2].string[1:-1])

    for title in html.find_all("h3"):
        if title.string=="Race information":
            title = title.parent.parent.find_all("div")[3]
            break

    for li in title.find_all("li"):
        try:
            res.append(li.find_all("div")[1].string)

        except IndexError:
            res.append("")

    return res

def find_race_top_10(page):
    tabs = page.find_all("table")
    a=0
    res = []

    try:
        for tab in tabs[0] :
            for line in tab.find_all("tr") :
                elems = line.find_all("td")
                i=0
                for elem in elems :
                    for lien in elem.find_all("a"):
                        if(len(str(lien.get("href")))>1):
                                if(str(lien.get("href"))[0]=="r" and str(lien.get("href"))[1]=="i" and str(lien.get("href"))[2]=="d" and str(lien.get("href"))[3]=="e" and str(lien.get("href"))[4]=="r" and str(lien.get("href"))[5]=="/"):	
                                    a=a+1
                                    res.append(lien.get_text())

                if(a>9):
                    break

    except IndexError:
        raise RaceCancelledError()
    return res

def main():
    top10 = []
    race_infos = []
    count = 1

    with open("out/races_url.txt", "r") as file:
        number_of_races = len(file.readlines())

    with open("out/races_url.txt", "r") as file:
        for line in file:
            print(f"\r{str(count)} / {str(number_of_races)}", end="")
            line = line[:-1]
            req = get(line)
            html = BeautifulSoup(req.text, "html.parser")

            try:
                top10.append(find_race_top_10(html))
                race_infos.append(find_race_info(html))

            except RaceCancelledError:
                pass

            count += 1

    col = ["nom", "circuit", "date", "heure_depart",
           "vitesse_moyenne", "categorie", "distance",
           "categorie2", "categorie3", "type_parcours",
           "score_denivele", "denivele", "ville_depart",
           "ville_arrivee", "rang_course", "score_qualite_ligne_depart",
           "maniere_gagner", "temperature"]
    col2 = ["premier", "deuxieme", "troisieme", "quatrieme",
            "cinquieme", "sixieme", "septieme", "huitieme",
            "neuvieme", "dixieme"]

    df = pd.DataFrame(race_infos,  columns=col)
    df1 = pd.DataFrame(top10, columns=col2)
    res = pd.concat([df, df1], axis=1)
    res.to_csv("out/courses2023.csv", encoding="utf-8", index=False)
    print()

if __name__=="__main__":
    main()

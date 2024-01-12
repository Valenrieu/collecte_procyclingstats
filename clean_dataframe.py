#!/bin/python3

import pandas as pd

def clean_races_file():
    df = pd.read_csv("out/courses2023.csv", encoding="utf-8")

    for row in range(len(df)):
        try:
            df.loc[row, "heure_depart"] = df.loc[row, "heure_depart"].split(" ")[0]

        except AttributeError:
            pass

        try:
            if df.loc[row, "vitesse_moyenne"]=="-":
                df.loc[row, "vitesse_moyenne"] = float("nan")

            else:
                df.loc[row, "vitesse_moyenne"] = df.loc[row, "vitesse_moyenne"].split(" ")[0]

        except AttributeError:
            pass

        try:
            if df.loc[row, "distance"]=="-":
                df.loc[row, "distance"] = float("nan")

            else:
                df.loc[row, "distance"] = df.loc[row, "distance"].split(" ")[0]

        except AttributeError:
            pass

        try:
            if df.loc[row, "temperature"]=="-":
                df.loc[row, "temperature"] = float("nan")

            else:
                df.loc[row, "temperature"] = df.loc[row, "temperature"].split(" ")[0]

        except AttributeError:
            pass

        if df.loc[row, "maniere_gagner"]=="? - let us know!":
            df.loc[row, "maniere_gagner"] = float("nan")

    df.drop(columns=["type_parcours"], axis=1, inplace=True)
    df.to_csv("out/courses2023.csv", encoding="utf-8", index=False)

if __name__=="__main__":
    try:
        clean_races_file()

    except KeyError:
        print("Le fichier ./out/courses2023.csv a deja ete modifie.")

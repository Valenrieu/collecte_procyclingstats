#!/bin/python3

import pandas as pd

def clean_races_file():
    listt = ["premier", "deuxieme", "troisieme", "quatrieme", "cinquieme",
             "sixieme", "septieme", "huitieme", "neuvieme", "dixieme"]

    df = pd.read_csv("out/courses2023.csv", encoding="utf-8", dtype={"rang_course":"Int32",
                     "score_denivele":"Int32", "score_qualite_ligne_depart":"Int32"})

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

        for col in listt:
            if pd.isna(df.loc[row, col]):
                pass

            else:
                temp = df.loc[row, col].split(" ")

                for item in range(len(temp)):
                    temp[item] = temp[item].capitalize()

                df.loc[row, col] = " ".join(temp)

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

    df.temperature.astype("Int16")
    df.drop(columns=["type_parcours"], axis=1, inplace=True)
    df.to_csv("out/courses2023.csv", encoding="utf-8", index=False)

if __name__=="__main__":
    try:
        clean_races_file()

    except KeyError:
        print("Le fichier ./out/courses2023.csv a deja ete modifie.")

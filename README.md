# Collecte de données sur [procyclingstats.com](https://www.procyclingstats.com)

## Introduction

***Mise à jour le 12/01/2024***

Nous avons décidé faire un état du lieu du cyclisme en 2023. Pour
ce faire, nous avons utilisé le site procyclingstats.com. C'est un
site dédié au cyclisme sur route. Nous avons récolté les données
des 500 meilleurs coureurs au [classement UCI](https://fr.wikipedia.org/wiki/Classement_mondial_UCI). Nous nous sommes aussi concentré
sur le résultat des courses les plus importantes, à savoir
les courses World Tour, les courses Pro Tour, les championnats
nationaux et mondiaux, et les courses du calendrier Europ Tour
les plus importantes (catégorie 1). Se référer à [ce guide](https://fr.wikipedia.org/wiki/Circuits_continentaux_de_cyclisme) pour comprendre les classifications des circuits continentaux. Les
indicateurs de classement sont les points UCI ou les points PCS,
à chaque course un nombre de points UCI est attribué aux premiers 
coureurs en fonction du classement, du barême et en fonction de la 
durée (courses d'un jour (classiques), courses d'une semaine et 
grand tours (Tour de France, Tour d'Italie et Tour d'Espagne qui 
durent 3 semaines)) et du prestige de la course. Les points PCS 
sont des points non officiels attribués par procyclingstats.com qui 
ont un barême différent de celui de l'UCI.

## Prérequis

Les dépendances du programme(pandas et bs4) sont disponibles dans 
le  fichier **requirements.txt**. Pour les installer avec pip, 
exécutez la commande :

```sh
pip install -r requirements.txt
```

## Organisation du projet

Le code source du projet est réparti dans plusieurs modules. Les
différents fichiers python sont disponibles à la racine du projet.
Le dossier **out** contient le répertoire cible pour les données.
Il contient 2 fichiers CSV et un fichier ASCII. Le fichier ASCII
contient toutes les urls nécessaire à la collecte des données
des courses, il est créé automatiquement par l'un des modules.
Les deux fichiers CSV sont les fichiers de données, il y en a un
relatif aux courses et l'autre relatif aux coureurs.

## Exécuter le script de collecte et de nettoyage

Le script a exécuter est le script **run.py**. Voici les
instructions pour les lancer sur différentes familles de
systèmes d'exploitation. Alternativement, vous pouvez exécuter
les fichiers un par un en respectant l'ordre, **export_races_url.py**,
**export_races_data.py**, **export_riders_data.py** et enfin
**clean_dataframe.py**.

### Unix

Pour lancer le script, rendez les fichiers exécutables :

```sh
chmod +x run.py clean_dataframe.py export_riders_data.py export_races_url.py export_races_data.py
```

Vous pouvez ensuite lancer le script avec la commande :

```sh
./run.py
```

### Windows

```bat
python3 run.py
```

ou

```bat
py run.py
```

dico_musiciens = [
    {
        "idmus": 12,
        "nom": "Parker",
        "prenom": "Charlie",
        "instru": "trompette",
        "idgrp": 96,
        "nb_concerts": 5,
    },
    {
        "idmus": 13,
        "nom": "Parker",
        "prenom": "Charlie",
        "instru": "trombone",
        "idgrp": 25,
        "nb_concerts": 9,
    },
    {
        "idmus": 58,
        "nom": "Dufler",
        "prenom": "Candy",
        "instru": "saxophone",
        "idgrp": 96,
        "nb_concerts": 4,
    },
    {
        "idmus": 97,
        "nom": "Miles",
        "prenom": "Davis",
        "instru": "saxophone",
        "idgrp": 87,
        "nb_concerts": 2,
    },
]


# Affichage de la liste de dictionnaires
print(dico_musiciens, end="\n\n")


def recherche_nom(tab):
    t = []
    for d in tab:
        if d["nb_concerts"] >= 4 and d["nom"] not in t:
            t.append(d["nom"])
    return t


# Test de la fonctions
reponse = recherche_nom(dico_musiciens)
print(reponse)

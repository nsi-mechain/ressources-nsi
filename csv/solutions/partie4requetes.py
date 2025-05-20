import csv

# Lecture du fichier CSV dans une liste de dictionnaires
with open('fichier.csv', 'rt', encoding='utf8') as f:
    lecteur = csv.DictReader(f, delimiter=',')
    donnees = list(lecteur)

# Personnes nées après 1970
for enregistrement in donnees:
    if int(enregistrement["Année de naissance"]) > 1970:
        print(enregistrement)

#Affichage des prénoms par âges croissants
donnees.sort(key=lambda x: x["Année de naissance"], reverse=True)
for enregistrement in donnees:
    print(enregistrement['Prénom'])

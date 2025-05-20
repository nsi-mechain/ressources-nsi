import csv

# Lecture du fichier CSV dans une liste de dictionnaires
with open('fichier.csv', 'rt', encoding='utf8') as f:
    lecteur = csv.DictReader(f, delimiter=',')
    donnees = list(lecteur)


print(donnees)  # affichage de la liste de dictionnaires


# Ecriture de la lmiste de dictionnaires dans un fichier CSV
with open('fichier2.csv', 'wt', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=donnees[0].keys())   
    writer.writeheader()    
    for dico in donnees:
        writer.writerow(dico)
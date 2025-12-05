*Terminale NSI*

![sqlite.jpg](sqlite.jpg)

# Contrôle SQL n°1

Vous utiliserez de préférence *sqlite3* en ligne de commande.

## ⮕ Rappel avec ce petit [tuto](exemple.md)

## ⮕ Exercice I : Création et modification d'une BDD

L'objectif est de créer une BDD `notes.db` avec une seule table `trimestre2` :

| Id | Nom     | Maths | Anglais | NSI |
|----|---------|-------|---------|-----|
| 1  | Alice   | 16    | 11      | 17  |
| 2  | Bob     | 12    | 15      | 10  |
| 3  | Charles | 9     | 11      | 18  |

### Donnez les commandes SQL permettant de :

1. Créer la table. **Attention** : la clé primaire sera **Id**, de type **INTEGER**
2. Remplissage de la table avec les trois enregistrements
3. Modifiez la note de maths d'Alice (18 au lieu de 16)
4. Supprimez complètement l'enregistrement  de *Bob* qui a changé d'établissement définitivement
5. Ajoutez le nouvel arrivant *Roger* (sans note)
6. Ajoutez un attribut SVT
7. Ajoutez une note de SVT aux élèves :
   - Alice : 15/20
   - Charles : 12/20
   - Roger : 17/20
8. Supprimez totalement et définitivement cette table (sans pour autant supprimer la BDD)

## ⮕ Exercice II- Requêtes SQL 

1. Créez une base de données *SQlite* nommée `bibio.db` à partir du script [create-biblio.sql](create-biblio.sql)
2. Affichez les titres des livres dont le titre contient **Astérix**
3. Affichez les titres et les années des albums d'Astérix aux éditions *Dargaud*
4. Idem triés par ordre d'année de parution
5. Affichez les titres des livres édités par les éditions *Robert Laffont* après 2015
6. Affichez le nombre de livres édités entre 1995 et 2000
7. Affichez le titre et l'année du plus ancien livre édité chez *Dargaud*
8. Affichez la liste des éditeurs, par ordre alphabétique, ayant produit au moins un livre avant 1980 (attention : un de ces éditeurs commence par une minuscule...)
9. Affichez **oui** ou **non** selon que les éditions *Hatier* possèdent ou non l'isbn 978-2218972324 (Essayez aussi votre requête SQL avec l'isbn 978-2218972325). Utilisez `IIF` (voir [ici](https://database.guide/how-iif-works-in-sqlite/))
10. Affichez, pour chaque éditeur, le nombre de livres publiés, par ordre de nombre de livres croissant, et à condition qu'aux moins **trois** livres aient été publiés.

Pour vous guider, voici les résultats devant être obtenus : [ici](resultats.txt)

## ⮕ Consignes

- Vous rendrez votre travail sous la forme de **deux fichiers texte** (nommés `exo1.sql` et `exo2.sql`).

- Pour le premier exercice, vous ajouterez à chaque commande SQL une deuxième commande permettant d'afficher la totalité de la table `trimestre2` (pour faciliter la correction)

- Vous pourrez utiliser des commandes internes à `sqlite3` comme indiqué dans le tuto.

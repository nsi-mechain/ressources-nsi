# Complexité des algorithmes

## I. Complexités de fonctions sur les [tableaux](https://fr.wikipedia.org/wiki/Tableau_(structure_de_donn%C3%A9es))

### 1) Tri par selection

a. Concevez une fonction de tri *par selection* d'un tableau de N entiers générés aléatoirement, et qui affiche le nombre d'itération i nécessaires au tri.

b. Faites une grande quantité de tests puis représentez graphiquement (tableur ou/et pyplot) i en fonction de N.

c. Vérifiez que  i = N(N-1)/2

d. Quelle est la [complexité](https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes) de cette méthode de tri ?

> Utilisez la notation **O(...)**.?

### 2) Recherche par parcours

a. Concevez une fonction permettant de retourner le nombre de fois qu'un entier est contenu dans une liste de N entiers générés aléatoirement.

b. Déterminez le nombre d'itérations nécessaires en fonction de N.

c. Déterminez la complexité de cette recherche.

### 3) Recherche dichotomique

a. Concevez une fonction retournant `True` si un entier e est présent dans un tableau de N entiers triés (`False` sinon), en utilisant une méthode [dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique). Cette fonction retournera aussi le nombre d'itérations effectuées.

b. Analysez *expérimentalement* puis *théoriquement* sa complexité.

## II. Complexité en [calcul numérique](https://fr.wikipedia.org/wiki/Calcul_num%C3%A9rique)

On se propose de rechercher une valeur approchée du [**zéro**](https://www.bibmath.net/dico/index.php?action=affiche&quoi=./r/racine.html) z (compris entre 2 et 4) de la fonction :

>`y = exp(-x) + sin(x)`

Tracez avec (en utilisant `matplotlib`) la courbe représentative de cette fonction, pour x variant de 2 à 4.

### 1) Recherche par balayage

Concevez une fonction *Python* qui, en partant de x=2 et en incrémentant de manière répétitive x par pas de 0.001 permette de retourner une valeur approchée de z et le nombre d'itérations nécessaires.

De quoi dépend ce nombre ?.

### 2) Recherche par dichotomie

Concevez une fonction permettant la recherche de z à 0.001 près par la [méthode de dichotomie](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_dichotomie), en partant de l'intervalle [2, 4]. Cette fonction devra aussi retourner le nombre d'itérations.

### 3) Complexités

Comparez les complexités (expérimentalement et théoriquement) de ces deux méthodes.

---
---

## ✍ À faire

Vous établirez un **notebook Jupyter** que vous déposerez dans un répertoire `complexite` de votre dépôt *GitHub*.





Terminale NSI - Lycée Pierre Méchain - Laon

# TP Graphes

## Travail à rendre :

Un notebook Jupyter dans votre dépôt GitHub contenant :

- les codes *Python*
- les explications (d'un point de vue algorithmique), des illustrations, etc. 
- au moins un exemple d'appel par méthode (avec le résultat)


vous utiliserez le graphe suivant :
[exemple de graphe](https://graphonline.top/fr?graph=nQopJixMMFCGYNlBZZcst)

## 1. Implémentation en *Python* d'une classe `Graphe`

Implémentez une classe `Graphe` permettant d'instancier des graphes de la façon suivante :

```python
mon_graphe = Graphe(matrice)
```

avec la matrice d'ajacence sous la forme suivante :

```python
matrice =   [
                [0, 1, 1, 1], 
                [1, 0, 1, 1], 
                [1, 1, 0, 0], 
                [1, 1, 0, 0]
            ]
```

Le seul attribut d'une instance sera nommé `matrice_adjacence`

## 2. Implémentations de quelques méthodes simples

1. une méthode `nombre_sommets()` qui retourne le nombre de sommets
2. une méthode `nombre_arretes_arcs()` qui retourne le nombre d'arrêtes et d'arcs (tuple)
3. une méthode `est_non_oriente()` qui renvoie `True` si le graphe est non-orienté
4. une méthode `liste_successeurs()` qui fournit une liste de listes
5. une méthode `liste_predecesseurs()` qui fournit une liste de listes

## 3 Implémentation des parcours

1. une méthode `parcours_BFS` qui prendra en argument l'indice du sommet de départ
2. une méthode `parcours_DFS` qui prendra en argument l'indice du sommet de départ
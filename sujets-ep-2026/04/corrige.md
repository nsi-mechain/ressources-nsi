# Corrigé de l'épreuve NSI - Sujet n°4

Ce document présente la correction des différentes questions du sujet. Le code Python complet testable se trouve dans le fichier `culture-corr.py` généré.

## Question 1 : Fonction `croissance_moyenne`

**Objectif :** Parcourir une liste d'objets `Plante`, récupérer leur attribut `croissance`, en calculer la somme pour enfin diviser par le nombre de plantes. Il faut aussi gérer le cas de la liste vide.

```python
def croissance_moyenne(liste_plantes):
    # Gestion du cas où la liste est vide
    if not liste_plantes:  # ou len(liste_plantes) == 0
        return None
        
    somme = 0
    # On parcourt les objets "Plante" (qui ont l'attribut .croissance)
    for plante in liste_plantes:
        somme += plante.croissance
        
    return somme / len(liste_plantes)
```

**Tests :**
```python
def test_croissance_moyenne():
    # Test 1 : Liste vide
    assert croissance_moyenne([]) == None
    # Test 2 : Jeu de données réel
    assert croissance_moyenne(plantes) == 79.0
```

---

## Question 2 : Fonction `dictionnaire_mesure`

**Objectif :** Créer un dictionnaire associant le nom de la plante (chaîne de caractères) à la liste de ses relevés de mesures.

```python
def dictionnaire_mesure(liste_plantes, liste_mesures):
    dico = {}
    
    # 1. On préremplit le dictionnaire avec toutes les plantes pour s'assurer 
    # que même les plantes sans mesures auront une liste vide associée.
    for plante in liste_plantes:
        dico[plante.nom] = []
        
    # 2. On alimente le dictionnaire avec les mesures.
    for mesure in liste_mesures:
        nom_de_la_plante = mesure['plante']
        # On vérifie si la plante existe dans le dictionnaire créé par précaution
        if nom_de_la_plante in dico:
            dico[nom_de_la_plante].append(mesure)
            
    return dico
```

---

## Question 3 : Analyse de l'erreur logique

Le code initial était :
```python
def purger_mesures_extremes(liste_mesures):
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            liste_mesures.remove(mesure)
    return liste_mesures
```

**Explication de l'erreur** :
On ne doit jamais modifier ni supprimer des éléments d'une liste pendant qu'on la parcourt avec une boucle `for` de la sorte.
En effet, la boucle `for` avance d'un indice à chaque itération. Si à l'itération `i` l'élément est supprimé avec `remove`, alors l'élément qui était à `i+1` est poussé à l'indice `i`.
Sauf qu'à l'itération suivante, la boucle analysera l'élément à l'indice `i+1`, c'est-à-dire l'élément qui était à la base en `i+2`.
L'élément à `i+1` qui a glissé vers la gauche a donc été "sauté" et n'est jamais vérifié. On s'en rend compte lorsqu'il y a deux mesures extrêmes qui se suivent, la deuxième ne sera pas supprimée.

---

## Question 4 : Correction de la fonction

Il existe plusieurs façons de contourner le problème décrit ci-dessus.

**Approche 1 : Créer une nouvelle liste (Recommandé en Python)**
L'approche la plus "propre" est de construire une nouvelle liste ne contenant que les éléments voulus (ceux qu'on garde) via une liste en compréhension. 
```python
def purger_mesures_extremes(liste_mesures):
    # On renvoie une nouvelle liste avec uniquement les bonnes mesures
    return [mesure for mesure in liste_mesures if 20 <= mesure['temperature'] <= 25]
```

**Approche 2 : Parcourir à l'envers (Modification en place de la liste d'origine)**
Si l'énoncé attend formellement que la liste mutée et retournée soit exactement le même espace de mémoire (la liste originale raccourcie), on utilise la technique de parcourir la liste en sens inverse. Ainsi, quand on supprime un élément et que les éléments qui le suivent sont décalés sur la gauche, ça n'affecte pas l'exploration des éléments précédents :
```python
def purger_mesures_extremes(liste_mesures):
    # On itère du dernier indice jusqu'à 0 pour éviter d'affecter le parcours 
    for i in range(len(liste_mesures) - 1, -1, -1):
        if liste_mesures[i]['temperature'] < 20 or liste_mesures[i]['temperature'] > 25:
            del liste_mesures[i]
    return liste_mesures
```

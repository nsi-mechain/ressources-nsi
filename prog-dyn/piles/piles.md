# Programmation dynamique — Exemple électronique : Sélection de piles pour obtenir une tension cible

## Problème

On dispose de piles de différentes tensions (par exemple : 1,5 V, 3 V, 9 V).  
On souhaite obtenir exactement une tension cible (par exemple : 12 V) en combinant ces piles **en série**,  
et utiliser **le moins de piles possible**.

---

## 1. Version récursive simple (sans mémoïsation)

```python
def min_piles_recursive(cible, tensions):
    if cible == 0:
        return 0
    if cible < 0:
        return float('inf')
    min_nombre = float('inf')
    for tension in tensions:
        nombre = 1 + min_piles_recursive(cible - tension, tensions)
        if nombre < min_nombre:
            min_nombre = nombre
    return min_nombre

# Exemple d'utilisation :
# print(min_piles_recursive(12, [1.5, 3, 9]))
```

---

## 2. Version récursive avec mémoïsation (top-down)

```python
def min_piles_top_down(cible, tensions, memo=None):
    if memo is None:
        memo = {}
    if cible == 0:
        return 0
    if cible < 0:
        return float('inf')
    if cible in memo:
        return memo[cible]
    min_nombre = float('inf')
    for tension in tensions:
        nombre = 1 + min_piles_top_down(cible - tension, tensions, memo)
        if nombre < min_nombre:
            min_nombre = nombre
    memo[cible] = min_nombre
    return min_nombre

# Exemple d'utilisation :
# print(min_piles_top_down(12, [1.5, 3, 9]))
```

---

## 3. Version itérative (bottom-up)

```python
def min_piles_bottom_up(cible, tensions):
    pas = 0.5  # Plus petite unité de tension (pour gérer les valeurs décimales)
    nb_etapes = int(cible / pas) + 1
    tableau = [float('inf')] * nb_etapes
    tableau[0] = 0
    for i in range(1, nb_etapes):
        valeur = i * pas
        for tension in tensions:
            if valeur - tension >= 0:
                indice = int((valeur - tension) / pas)
                tableau[i] = min(tableau[i], tableau[indice] + 1)
    indice_cible = int(cible / pas)
    return tableau[indice_cible] if tableau[indice_cible] != float('inf') else -1

# Exemple d'utilisation :
# print(min_piles_bottom_up(12, [1.5, 3, 9]))
```

---

## Remarques

- **Valeur de retour** : Si la fonction retourne `float('inf')` (ou `-1` pour la version itérative), cela signifie qu’il est **impossible d’atteindre la tension cible** avec les piles disponibles.

- **Choix du pas** : Pour gérer les tensions avec virgule (1,5 V), on utilise un pas (par exemple 0,5 V).  
  Il faut que toutes les tensions soient des multiples du pas choisi.

- **Complexité** :
  
  - La version récursive simple est peu efficace sur de grandes cibles.
  
  - La version mémoïsée et la version itérative sont recommandées pour des cas plus complexes.

---

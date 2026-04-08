# Calcul du nombre de chemins dans une matrice

## Énoncé du problème

On considère une grille (ou matrice) de dimensions $m \times n$. 
Un robot se trouve dans la case située dans le coin supérieur gauche (de coordonnées `(1, 1)`) et doit atteindre la case située dans le coin inférieur droit (de coordonnées `(m, n)`).

À chaque étape, le robot ne peut effectuer que deux types de mouvements :
1. Se déplacer d'une case vers la **droite**.
2. Se déplacer d'une case vers le **bas**.

Votre objectif est de calculer le **nombre total de chemins uniques** permettant d'aller du point de départ au point d'arrivée.

### Exemple
Pour une grille de dimensions $2 \times 3$, le robot doit aller de `(1, 1)` à `(2, 3)`.
Il y a exactement **3** chemins distincts :
1. Droite $\rightarrow$ Droite $\rightarrow$ Bas
2. Droite $\rightarrow$ Bas $\rightarrow$ Droite
3. Bas $\rightarrow$ Droite $\rightarrow$ Droite

---

## Travail à réaliser

Vous allez implémenter la solution du problème en utilisant la **programmation dynamique**. Pour bien comprendre l'apport de la mémoïsation, nous allons compter le nombre d'appels à la fonction nécessaires pour trouver le résultat final avec différentes approches.

La variable globale `ctr` nous servira de compteur.

Complétez les 4 fonctions définies ci-dessous :

```python
# 1. Récursivité classique (naïve)
def nr(m, n):
    """
    Calcule le nombre de chemins de façon récursive pure, sans optimisation.
    Cas de base : s'il n'y a qu'une seule ligne ou une seule colonne, il n'y a qu'un seul chemin.
    """
    global ctr; ctr += 1
    
    # ... À compléter ...
    pass


# 2. Mémoïsation avec un dictionnaire (passé en paramètre)
def nm(m, n, memo=None):
    """
    Calcule le nombre de chemins en utilisant un dictionnaire `memo` 
    pour stocker les résultats des sous-problèmes déjà calculés afin d'éviter 
    de les recalculer plusieurs fois.
    """
    global ctr; ctr += 1
    if memo is None:
        memo = {}
        
    # ... À compléter ...
    pass


# 3. Mémoïsation avec un tableau de tableaux (liste de listes)
def nm_liste(m, n, memo=None):
    """
    Calcule le nombre de chemins en utilisant une structure de tableaux imbriqués 
    pour stocker les résultats des sous-problèmes.
    """
    global ctr; ctr += 1
    if memo is None:
        # Initialisation d'une matrice de dimensions (m+1)x(n+1) remplie de None
        memo = [[None for _ in range(n+1)] for _ in range(m+1)]
        
    # ... À compléter ...
    pass


# 4. Mémoïsation transparente avec le décorateur functools.cache
from functools import cache

@cache
def nc(m, n):
    """
    Calcule le nombre de chemins de façon récursive en utilisant le décorateur @cache 
    de Python. La mémoïsation est gérée automatiquement par le langage.
    """
    global ctr; ctr += 1
    
    # ... À compléter ...
    pass


# ==============================================================================
# Code de test fourni
# Exécutez ce code une fois vos fonctions codées pour comparer leurs performances
# ==============================================================================

if __name__ == "__main__":
    for f in nr, nm, nm_liste, nc:
        ctr = 0
        result = f(12, 15)  # Test sur une matrice 12x15
        print(f"--- Méthode appelée : {f.__name__} ---")
        print(f"Résultat attendu : {result}")
        print(f"Nombre d'appels à la fonction : {ctr}\n")
```

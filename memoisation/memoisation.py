# Récursivité classique
def nr(m, n):
    if m == 1 or n == 1:  # cas de base : une seule ligne ou une seule colonne
        return 1
    else:
        return nr(m-1, n) + nr(m, n-1)  # appel récursif


# avec dictionnaire de mémoïsation passé en paramètre de la fonction récursive
def nm(m, n, memo=None):
    # Initialisation du dictionnaire de mémoïsation lors du premier appel
    if memo is None:
        memo = {}
    # Cas de base : une seule ligne ou une seule colonne
    if m == 1 or n == 1:
        memo[(m, n)] = 1
        return 1
    # Vérifier si le résultat a déjà été calculé
    if (m, n) in memo:
        return memo[(m, n)]
    # Appel récursif et mémorisation du résultat
    memo[(m, n)] = nm(m - 1, n, memo) + nm(m, n - 1, memo)
    return memo[(m, n)]


# avec functools.cache
from functools import cache
@cache
def nc(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return nc(m-1, n) + nc(m, n-1)


##################################################################################################
# Mesure des durées d'exécution
import time

for f in (nr, nm, nc):
    start = time.time()
    result = f(10,20)
    end = time.time()
    print(f'Résultat : {result}')
    print(f'Durée : {end-start}')
    print()



# Récursivité classique (sans mémoïsation) — très inefficace pour de grandes valeurs
def nr(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return nr(m-1, n) + nr(m, n-1)


# Mémoïsation explicite avec dictionnaire (top-down)
def n_dyn_dico(m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 1 or n == 1:
        memo[(m, n)] = 1
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = n_dyn_dico(m - 1, n, memo) + n_dyn_dico(m, n - 1, memo)
    return memo[(m, n)]


# Mémoïsation explicite avec matrice (top-down)
def n_dyn_liste(m, n, memo=None):
    if memo is None:
        memo = [[None for _ in range(n+1)] for _ in range(m+1)]
    if m == 1 or n == 1:
        memo[m][n] = 1
        return 1
    if memo[m][n] is not None:
        return memo[m][n]
    memo[m][n] = n_dyn_liste(m-1, n, memo) + n_dyn_liste(m, n-1, memo)
    return memo[m][n]


# Programmation dynamique bottom-up avec matrice complète
def n_dyn_bot_up(m, n):
    table = [[0] * n for _ in range(m)]
    for i in range(m):
        table[i][0] = 1
    for j in range(n):
        table[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]


# Programmation dynamique bottom-up optimisée en espace (tableau 1D)
def n_dyn_bot_up_opti(m, n):
    ligne = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            ligne[j] += ligne[j - 1]
    return ligne[n - 1]


# Mémoïsation implicite avec @cache (top-down)
from functools import cache

@cache
def n_cache(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return n_cache(m - 1, n) + n_cache(m, n - 1)


# Mesure des durées d'exécution pour chaque méthode avec m=12, n=15
import time

fonctions = (
    ("Récursivité simple", nr),
    ("Dictionnaire (top-down)", n_dyn_dico),
    ("Matrice (top-down)", n_dyn_liste),
    ("Bottom-up", n_dyn_bot_up),
    ("Bottom-up optimisée", n_dyn_bot_up_opti),
    ("@cache (top-down)", n_cache)
)

for nom, f in fonctions:
    start = time.time()
    result = f(14, 18)
    end = time.time()
    print(f"{nom}")
    print(f"Résultat : {result}")
    print(f"Durée : {(end-start)*1e6:.2f} μs\n")


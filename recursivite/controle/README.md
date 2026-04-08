Terminale NSI

# Contrôle sur la récursivité
---
## Exercice 1 (2 points)

Écrire la fonction `puissance(x, n)` qui calcule x<sup>n</sup> pour tout entier naturel n.

1. de façon **itérative**
2. de façon **récursive**
---
## Exercice 2 *(2 points)*

Soit la fonction `recur1(n: int) -> int` :

```python
def recur1(n):
   if n == 0:
       return 0
   else:
       return n + recur1(n-1)
```

1. Que retourne l'appel `recur1(0)` ?
2. Que retourne l'appel `recur1(1)` ?
3. Que retourne l'appel `recur1(2)` ?
4. Que retourne l'appel `recur1(3)` ?
5. Cas général : que retourne `recur1(n)` ?
---
## Exercice 3 *(2 points)*

Soit la fonction `recur2(n: int, m: int) -> None` :

```python
def recur2(n, m):
    if n > m:
        print()
        return
    else:
        print(n, end=' ')
        recur2(n+1, m)
```

1) Qu'affiche l'appel `recur2(1, 0)` ?
2) Qu'affiche l'appel `recur2(0, 1)` ?
3) Qu'affiche l'appel `recur2(20, 23)` ?
4) Combien de fois **au maximum** cette fonction est-elle présente dans la **pile d'appel** en fonction de n et m (on suppose que n<m) ?
---
<div style="page-break-after: always;"></div>

## Exercice 4 *(2 points)*

Soit la fonction `recur3(n: int, m: int) -> None` :

```python
def recur3(n, m):
    if n > m:
        return
    else:
        print(n, m)
        recur3(n+1, m-1)
```

1) Qu'affiche l'appel `recur3(4, 6)` ?
2) Qu'affiche l'appel `recur3(4, 7)` ?
3) Qu'affiche l'appel `recur3(4, 4)` ?
4) Qu'affiche l'appel `recur3(4, 3)` ?
5) Que doit-on modifier dans ce code pour que l'on ait **jamais** l'affichage de deux entiers **égaux** sur la même ligne ?
---
## Exercice 5 *(6 points)*

On définit les fonctions `Koch` et `flocon` suivantes :

```python
from turtle import *


def Koch(n, d):
    if n == 0:
        forward(d)
    else:
        Koch(n-1, d/3)
        left(60)
        Koch(n-1, d/3)
        right(120)
        Koch(n-1, d/3)
        left(60)
        Koch(n-1, d/3)


def flocon(n, d):
    for k in range(3):
        Koch(n, d)
        right(120)

```

*Pour répondre aux questions suivantes, vous utiliserez sur votre copie une échelle de 2cm/100pix*

1. Dessinez le résultat de l'appel `Koch(1, 300)`
2. Quelle est la largeur de cette figure, en pixels ? *(on rappelle que cos(60°)=0,5)*
3. Dessinez le résultat de l'appel `Koch(2, 300)`
4. Quelle est la largeur de cette figure, en pixels ?
5. Dessinez le résultat de l'appel `flocon(0, 300)`
6. Dessinez le résultat de l'appel `flocon(1, 300)`

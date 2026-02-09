# Exercice : Manipulation de piles et de files

On rappelle :  
- Une **file (queue)** suit la discipline **FIFO** : *First In, First Out*.  
  - Primitives : `est_vide()`, `enfiler(x)`, `défiler()`.  
- Une **pile (stack)** suit la discipline **LIFO** : *Last In, First Out*.  
  - Primitives : `est_vide()`, `empiler(x)`, `dépiler()`.

On dispose de deux structures de données selon les situations :  
- F1, F2 : **files**  
- P1, P2 : **piles**

Les éléments sont des chaînes de caractères.

---

## Travail demandé

Pour chaque situation :

1. **Dessiner** l’état des structures après chaque opération (schémas).  
2. **Décrire l’algorithme** en pseudo-code.  
3. **Écrire le code Python** correspondant, *uniquement avec les primitives demandées*.  
4. **Déterminer le contenu final de la structure initiale*.*

---

## Situation 1 — Deux files

La file **F1** contient initialement (avant → arrière) :
```
a, b, c
```
La file **F2** est vide.

### Opérations
1. On vide **F1** dans **F2**.  
2. On vide ensuite **F2** dans **F1**.

**Question :** Quel est le contenu final de F1 ?

---

## Situation 2 — Deux piles

La pile **P1** contient initialement (sommet → bas) :
```
a, b, c
```
La pile **P2** est vide.

### Opérations
1. On vide **P1** dans **P2**.  
2. On vide ensuite **P2** dans **P1**.

**Question :** Quel est le contenu final de P1 ?

---

## Situation 3 — Une pile et une file

La pile **P1** contient initialement :
```
a, b, c
```
La file **F2** est vide.

### Opérations
1. On vide **P1** dans **F2**.  
2. On vide ensuite **F2** dans **P1**.

**Question :** Quel est le contenu final de P1 ?

---

## Situation 4 — Une file et une pile

La file **F1** contient initialement :
```
a, b, c
```
La pile **P2** est vide.

### Opérations
1. On vide **F1** dans **P2**.  
2. On vide ensuite **P2** dans **F1**.

**Question :** Quel est le contenu final de F1 ?

---

## Consignes

- Les schémas seront réalisés en ASCII avec la norme :  

      Une file :
      F1 : in> [c] [b] [a] >out

      Une pile :
      P1 : in/out<> [c] [b] [a]
- Le pseudo-code doit respecter strictement les primitives :  
  - `est_vide()`  
  - `enfiler(x)` / `défiler()`  
  - `empiler(x)` / `dépiler()`  
- Le code Python doit se limiter aux mêmes primitives.



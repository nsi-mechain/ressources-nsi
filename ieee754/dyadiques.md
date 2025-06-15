# Fractions dyadiques et représentation binaire

## 1. Qu’est-ce qu’une fraction dyadique ?

Une **fraction dyadique** est un nombre qui peut s’écrire sous la forme :

    k / 2ⁿ

où :

- k est un entier (positif ou négatif),
- n est un entier naturel (0, 1, 2, ...).

**Exemples :**

- 3/8  = 3 / 2³
- 5/2  = 5 / 2¹
- 1    = 1 / 2⁰
- 0,625 = 5 / 8 = 5 / 2³

---

## 2. Lien avec la représentation binaire

En binaire, on écrit un nombre comme une somme de puissances négatives de 2 :

    a0 + a1 * (1/2) + a2 * (1/4) + ... + an * (1/2ⁿ)

où chaque ai vaut 0 ou 1.

**Exemple :**
Le nombre 1,101₂ (en binaire) correspond à :

- 1 (partie entière)
- 1 * 1/2 = 0,5
- 0 * 1/4 = 0
- 1 * 1/8 = 0,125

Total : 1 + 0,5 + 0 + 0,125 = **1,625**

---

## 3. Propriété importante

- Tous les nombres ayant une écriture binaire finie sont des **fractions dyadiques**.
- Certains nombres décimaux simples (comme 0,1) n’ont pas d’écriture binaire finie : ils ne sont pas des fractions dyadiques.

---

## 4. Résumé

- Une fraction dyadique s’écrit **k / 2ⁿ**.


# TP NSI – RSA avec micro:bit : Paul, Alice et le Pirate

## Présentation

Dans ce TP, vous allez simuler une communication chiffrée entre deux micro:bit v2 à l’aide du chiffrement **RSA** et de la **liaison radio**.

Un troisième micro:bit joue le rôle d’un **pirate** qui intercepte la transmission et tente de retrouver le message.

L’objectif est de comprendre :

* le fonctionnement du chiffrement RSA
* la différence entre clé publique et clé privée
* pourquoi RSA est fragile avec de petits nombres

---

## Organisation

Travail par **trinôme** :

* **Alice** : génère les clés RSA et reçoit les messages
* **Paul** : chiffre un message et l’envoie
* **Pirate** : intercepte et attaque la transmission

Chaque élève programme son propre micro:bit.

---

## Contraintes

* Message : entier entre **2 et 99**
* Nombres premiers : **≤ 50**
* MicroPython sur micro:bit v2
* Communication par **radio micro:bit**
* Inverse modulaire par **recherche exhaustive**

---

## Rappel sur RSA

Alice choisit deux nombres premiers **p** et **q** :

```
n = p × q
φ(n) = (p − 1)(q − 1)
```

Elle choisit **e** premier avec φ(n) et calcule **d** tel que :

```
e × d ≡ 1 (mod φ(n))
```

* Clé publique : (e, n)
* Clé privée : (d, n)

Paul chiffre :

```
c = m^e mod n
```

Alice déchiffre :

```
m = c^d mod n
```

---

## Protocole radio

Les micro:bits communiquent par messages texte :

* Alice → Paul :

  ```
  PUB;e;n
  ```

* Paul → Alice :

  ```
  CIPH;c
  ```

Le pirate écoute **tous les messages radio**.

---

# Travail demandé

## 1. Programme d’Alice

Alice doit :

1. Choisir deux nombres premiers p et q
2. Calculer les clés RSA
3. Envoyer la clé publique par radio
4. Recevoir le message chiffré
5. Le déchiffrer et l’afficher

---

## 2. Programme de Paul

Paul doit :

1. Recevoir la clé publique
2. Choisir un message m
3. Le chiffrer
4. Envoyer le message chiffré

---

## 3. Programme du Pirate

Le pirate doit :

1. Écouter les messages radio
2. Récupérer (e, n) et c
3. Factoriser n
4. Recalculer la clé privée
5. Retrouver le message

---

## Méthode d’attaque

Le pirate teste tous les diviseurs possibles :

```
pour i de 2 à n :
    si n % i == 0 :
        p = i
        q = n // i
```

Puis il reconstruit la clé privée.

---

## Résultat attendu

* Alice affiche le message déchiffré
* Paul affiche le message envoyé
* Le pirate affiche le message retrouvé

Les trois résultats doivent être identiques.

---

## Questions

1. L’attaque du pirate est-elle rapide ?
2. Pourquoi fonctionne-t-elle ici ?
3. Que se passerait-il avec de très grands nombres ?
4. Comment améliorer la sécurité ?

---

## Bonus (facultatif)

* Ajouter un padding simple
* Envoyer plusieurs messages
* Mesurer le temps d’attaque
* Tester différentes tailles de nombres

# 🧠 TP – Jeu de chiffrement RSA (binôme Paul & Alice)

## 🎯 Objectif
Découvrir le **chiffrement asymétrique RSA** en manipulant des nombres à la calculatrice.
Le message à transmettre est un **entier strictement inférieur à 100**.

---

## 👥 Rôles
- **Alice** : crée les clés, conserve la clé privée, déchiffre
- **Paul** : chiffre le message avec la clé publique

---

## 🟥 Étape 1 – Choix des nombres secrets (Alice)

Alice choisit **deux nombres premiers distincts**, notés p et q.

**Contraintes :**
- p différent de q
- p et q doivent être premiers
- pour le jeu, ils doivent être choisis **uniquement dans la liste suivante**

**Liste complète des valeurs possibles :**
11, 13, 17, 19, 23, 29

👉 **Ne pas noter p et q.**  
Une fois les clés calculées, **on peut oublier p et q**.

---

## 🟥 Étape 2 – Calculs RSA (Alice)

Calculer :
- n = p × q
- φ(n) = (p − 1) × (q − 1)

---

## 🟩 Étape 3 – Clé publique (Alice → Paul)

Choisir un entier e tel que :
- 1 < e < φ(n)
- e et φ(n) sont premiers entre eux (PGCD = 1)

Valeurs conseillées : **3, 5, 7, 11**

👉 La **clé publique** est le couple **(n, e)**  
👉 La noter sur le **post-it vert** et la donner à Paul.

---

## 🟥 Étape 4 – Clé privée (Alice)

Trouver un entier d tel que :
- e × d donne un reste de 1 lorsqu’on divise par φ(n)

Méthode : tester des valeurs de d jusqu’à obtenir un reste égal à 1.

👉 La **clé privée est le nombre d**, à noter sur le **post-it rouge**.

---

## 🟩 Étape 5 – Chiffrement (Paul)

1. Choisir un message m inférieur à 100
2. Calculer le message chiffré :
- c = (m puissance e) modulo n

👉 Noter le message chiffré **c** sur un **post-it orange** et le donner à Alice.

---

## 🟥 Étape 6 – Déchiffrement (Alice)

Calculer le message clair :
- m = (c puissance d) modulo n

👉 Annoncer le message retrouvé.

---

## ✅ À retenir
- **Clé publique** : n et e → post-it **vert**
- **Clé privée** : d → post-it **rouge**
- **Message chiffré** : c → post-it **orange**
- Les nombres p et q servent uniquement à fabriquer les clés et peuvent être oubliés
- La sécurité de RSA repose sur la difficulté de retrouver p et q à partir de n


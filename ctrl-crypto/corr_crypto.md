# Corrigé

## 1) Chiffrement XOR

### a) XOR bit à bit détaillé :
Message : 1010110010  
Clé : 1101001001

1 XOR 1 = 0  
0 XOR 1 = 1  
1 XOR 0 = 1  
0 XOR 1 = 1  
1 XOR 0 = 1  
1 XOR 0 = 1  
0 XOR 1 = 1  
0 XOR 0 = 0  
1 XOR 0 = 1  
0 XOR 1 = 1  

Message chiffré : 0111111011

### b) Déchiffrement XOR détaillé :
Texte chiffré : 0111111011  
Clé : 1101001001

0 XOR 1 = 1  
1 XOR 1 = 0  
1 XOR 0 = 1  
1 XOR 1 = 0  
1 XOR 0 = 1  
1 XOR 0 = 1  
1 XOR 1 = 0  
0 XOR 0 = 0  
1 XOR 0 = 1  
1 XOR 1 = 0  

Message déchiffré : 1010110010

---

## 2) Chiffrement RSA : généralités

- Question 1 : Réponse B : Factorisation de grands nombres premiers.
- Question 2 : Réponse C : Liées mathématiquement mais difficiles à déduire.
- Question 3 : Réponse A : Deux grands nombres premiers.
- Question 4 : Réponse C : Pour chiffrer un message avec la clé publique.
- Question 5 : Réponse B : Car les ordinateurs ne peuvent pas factoriser rapidement de grands nombres.

---

## 3) RSA en Python

### 3.1) Calcul des clés RSA détaillé

#### a) Calcul précis :
- n = p × q = 3 × 11 = 33  
- phi(n) = (p-1) × (q-1) = 2 × 10 = 20

#### b) Vérification détaillée de l'inverse modulaire d :
On cherche d tel que (d × e) mod 20 = 1

- d=2 : (2×3) mod 20=6  
- d=3 : (3×3) mod 20=9  
- d=4 : (4×3) mod 20=12  
- d=5 : (5×3) mod 20=15  
- d=6 : (6×3) mod 20=18  
- d=7 : (7×3) mod 20=1 ⇒ d=7 trouvé

La boucle for sert à trouver l'inverse modulaire en testant chaque valeur.

#### c) Différence clés publique/privée :
- Clé publique : (3,33), clé privée : (7,33). Différentes car RSA est asymétrique.

### 3.2) Chiffrement/déchiffrement

- Message original : 5

#### 3.2.1) Chiffrement :
5^3 mod 33 = 125 mod 33 = 26

#### 3.2.2) Déchiffrement :
26^7 mod 33 = 5

#### 3.2.3) Pourquoi retrouve-t-on le message original :
RSA utilise des exposants inverses modulo phi(n).

#### 3.2.4) Déchiffrement avec clé publique :
Impossible, résultat incohérent car RSA est asymétrique par conception.

---

## 4) Chiffrement affine

### 4.1) Vérification clé affine

PGCD(a,26) :
- a=5 : PGCD(5,26)=1 ⇒ inversible
- a=6 : PGCD(6,26)=2 ⇒ non inversible
- a=7 : PGCD(7,26)=1 ⇒ inversible

Couples valides : (5,8), (7,15)

### 4.2) Chiffrement affine (A=0, B=1, etc.)

#### Chiffrement de « CASSIS » avec clé (5,8) :
| Lettre | C | A | S | S | I | S |
|--------|---|---|---|---|---|---|
| Rang   | 2 | 0 | 18| 18| 8 | 18|
| Calcul |(5×2+8)=18|(5×0+8)=8|(5×18+8)=98|(5×18+8)=98|(5×8+8)=48|(5×18+8)=98|
| Résultat mod 26|18|8|20|20|22|20|
| Lettre chiffrée|S|I|U|U|W|U|

Résultat final : SIUUWU

#### Déchiffrement « VUW » avec clé inverse (21,8) :
Inverse modulaire vérifié : 5×21=105 mod 26=1

| Lettre | V | U | W |
|--------|---|---|---|
| Rang   | 21| 20| 22|
| Calcul |21×(21-8)=273|21×(20-8)=252|21×(22-8)=294|
| Résultat mod 26|13|18|8|
| Lettre déchiffrée|N|S|I|

Résultat final : NSI

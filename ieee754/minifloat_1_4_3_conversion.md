# 📘 Minifloat (1,4,3)

## 📌 Paramètres du format

* **1 bit signe** (s)
* **4 bits exposant** (E), biais = 7
* **3 bits mantisse** (M)

### Cas particuliers

* `E = 0000` : dénormalisés (pas de bit implicite, exposant effectif = −6)
* `E = 1111, M = 000` : ±∞
* `E = 1111, M ≠ 000` : NaN (Not a Number)

---

## 🔎 Définition : ULP

* **ULP (Unit in the Last Place)** = l’écart entre deux nombres consécutifs représentables.
* Sa valeur dépend de l’exposant réel utilisé :

  * Pour un exposant réel **e**, on a ULP = 2^(e − 3) car la mantisse possède 3 bits.
* Exemple :

  * à e = −6 ⇒ ULP = 2^(−9) = 0,001953125
  * à e = 7 ⇒ ULP = 2^(4) = 16

**Rôle de l’ULP** :

* Lors d’un arrondi, on choisit le nombre flottant le plus proche.
* Si la valeur réelle est exactement à **½ ULP** de deux représentations, on applique la règle du **ties-to-even** (on choisit celui dont la mantisse est paire).

---

## 🚀 Algorithme de conversion (avec log₂)

1. **Signe** : s = 0 si x ≥ 0, s = 1 sinon.

2. **Cas spéciaux** :

   * x = 0 ⇒ `s 0000 000`
   * x → ±∞ ⇒ `s 1111 000`
   * NaN ⇒ `0 1111 M≠000`

3. **Normalisation** :

   * a = |x|
   * e = ⌊log₂(a)⌋
   * m = a / 2^e (donc 1 ≤ m < 2)
   * Si −6 ≤ e ≤ 7 :

     * Exposant codé : E = e + 7 (sur 4 bits)
     * Mantisse : (m−1)×2^3 arrondie au plus proche (ties-to-even)
   * Si e < −6 : on passe en dénormalisé
   * Si e > 7 : overflow ⇒ ±∞

4. **Dénormalisés (E=0000)** :

   * Valeur = (M/8) × 2^(−6)
   * Mantisse choisie par arrondi de a×512

5. **Assemblage** :

   * Normalisé : `s EEEE MMM`
   * Dénormalisé : `s 0000 MMM`
   * Infini : `s 1111 000`

6. **Décodage** :

   * Normalisé : (1+M/8) × 2^(E−7)
   * Dénormalisé : (M/8) × 2^(−6)

---

## ✅ Exemples détaillés

### A) Petit normalisé : x = 0,02

1. s = 0
2. log₂(0,02) ≈ −5,64 ⇒ e = −6
3. m = 0,02 × 64 = 1,28
4. Mantisse = (0,28×8) ≈ 2,24 ⇒ arrondi = 2 ⇒ `010`
5. Exposant codé = −6 + 7 = 1 ⇒ `0001`
6. Mot binaire = `0 0001 010`
7. Valeur stockée = 0,01953125

### B) Grand normalisé : x = 100

1. s = 0
2. log₂(100) ≈ 6,64 ⇒ e = 6
3. m = 100 / 64 = 1,5625
4. Mantisse = (0,5625×8) = 4,5 ⇒ arrondi ties-to-even ⇒ 4 ⇒ `100`
5. Exposant codé = 6+7 = 13 ⇒ `1101`
6. Mot binaire = `0 1101 100`
7. Valeur stockée = 96 (car ULP = 8, et 100 est à 0,5 ULP de 96 → mantisse paire retenue)

### C) Dénormalisé : x = 0,014

1. s = 0
2. log₂(0,014) ≈ −6,16 ⇒ e < −6 ⇒ dénormalisé
3. M = arrondi(0,014×512) = arrondi(7,168) = 7 ⇒ `111`
4. Mot binaire = `0 0000 111`
5. Valeur stockée = 0,013671875

### D) Infini : x = 1000

1. s = 0
2. log₂(1000) ≈ 9,97 ⇒ e > 7 ⇒ overflow
3. Mot binaire = `0 1111 000`
4. Valeur stockée = +∞

---

## 📊 Repères numériques

* Plus petit normalisé : 2^(−6) = 0,015625
* Plus grand dénormalisé : (7/8)×2^(−6) = 0,013671875
* Frontière dénorm ↔ normal : 0,0146484375
* Max normalisé : (1+7/8)×2^7 = 240
* ULP au max : 16
* Seuil vers +∞ = 240 + ½·ULP = 248

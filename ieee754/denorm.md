# 📌 Mémo : Calcul de la mantisse pour les dénormalisés

## 1. Rappel
Dans un format flottant (s, e, m) :
- s = bits de signe
- e = bits d’exposant
- m = bits de mantisse
- biais = 2^(e−1) − 1

### Cas dénormalisé
- Exposant codé = `000…0`
- Pas de 1 implicite
- Exposant effectif fixé à 1 − biais

La valeur représentée est :

```
Valeur = (M / 2^m) × 2^(1 − biais)
```

---

## 2. Mise sous forme pratique
En regroupant :

```
Valeur = M × 2^( (1 − biais) − m )
```

Ainsi, pour approximer x par un dénormalisé :

```
M ≈ x × 2^( m + biais − 1 )
```

Puis on arrondit M (arrondi au plus proche, ties-to-even).

---

## 3. Exemple : format (1,4,3)
- e = 4 → biais = 7
- m = 3
- Exposant effectif = 1 − 7 = −6
- Formule :

```
M ≈ x × 2^( m + biais − 1 )
  = x × 2^(3 + 7 − 1)
  = x × 2^9
  = x × 512
```

### Application : x = 0,014
```
M ≈ 0,014 × 512 = 7,168
Arrondi → 7 → 111
Valeur = 7 × 2^(-9) = 0,013671875
```

---

## 4. Généralisation
- Plus le nombre de bits de mantisse augmente, plus on multiplie par une puissance de 2 élevée pour trouver M.
- La règle **M ≈ x × 2^(m + biais − 1)** est valable pour tout format (s, e, m).

---

✅ **À retenir** : le multiplicateur (comme 512 dans (1,4,3)) vient de la combinaison *mantisse_bits + biais − 1*. C’est ce qui permet de retrouver la mantisse des dénormalisés.


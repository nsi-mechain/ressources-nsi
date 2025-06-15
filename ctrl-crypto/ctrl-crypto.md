Terminale NSI - Lycée Pierre Méchain

# Cryptographie

## 1) Chiffrement XOR

On souhaite chiffrer un message binaire à l’aide d’une clé binaire de même longueur en utilisant **l’opération XOR bit à bit**.

#### Données

- **Message binaire** :
  
  `message = 1010110010`

- **Clé binaire** :
  
  `cle = 1101001001`

a) Appliquez un XOR bit à bit entre le message et la clé pour obtenir le **message chiffré**

b) Appliquez à nouveau un XOR entre le texte chiffré et la clé pour retrouver le **message original**.

## 2) chiffrement RSA : généralités

#### **Question 1 :**

Quel est le principe de base du chiffrement RSA ?  

- A. Utiliser une clé symétrique pour chiffrer et déchiffrer le message  
- B. Utiliser la factorisation de grands nombres premiers  
- C. Compresser les messages pour les sécuriser  
- D. Utiliser une clé partagée entre l’émetteur et le récepteur  

#### **Question 2 :**

Dans RSA, quelle est la relation entre la clé publique et la clé privée ?  

- A. Elles sont identiques  
- B. Elles sont toutes deux choisies au hasard  
- C. Elles sont liées mathématiquement, mais l’une ne permet pas de déduire facilement l’autre  
- D. La clé publique est dérivée de la clé privée par un hachage  

#### **Question 3 :**

Quels nombres sont utilisés pour générer une paire de clés RSA ?  

- A. Deux grands nombres premiers  
- B. Deux nombres consécutifs
- C. Un nombre pair et un nombre impair 
- D. Deux puissances de 2  

#### **Question 4 :**

À quoi sert l’exposant `e` dans la clé publique RSA ?  

- A. Il est utilisé pour générer les nombres premiers  
- B. Il permet de déchiffrer un message  
- C. Il est utilisé pour chiffrer un message avec la clé publique  
- D. Il empêche le chiffrement d’un message nul  

#### **Question 5 :**

Pourquoi RSA est-il considéré comme sécurisé (en pratique) ?  

- A. Parce qu’il est très ancien  
- B. Parce que les ordinateurs ne peuvent pas factoriser rapidement de grands nombres
- C. Parce qu’il utilise des lettres au lieu de chiffres  
- D. Parce qu’il change de clé toutes les secondes

## 3) chiffrement RSA : programmation _Python_

On se propose d'étudier un chiffrement / déchiffrement **RSA** en utilisant des **petits** nombres de manière à pouvoir vérifier les différentes étapes "à la main".

Le message à chiffrer (puis déchiffrer) va être un **entier positif** (5).

### 3.1) Calcul des clés

```python
# Choix de petits nombres premiers p et q
p = 3
q = 11
# Choix d'un exposant e (doit être premier avec φ(n))
e = 3

# Calcul de n et de φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Calcul de d (l'inverse modulaire de e modulo φ(n))
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

d = mod_inverse(e, phi)

# Clés générées
cle_pub = (e, n)
cle_priv = (d, n)
```

a) Donnez les valeurs de `n` et `phi`

b) Montrez que `d` contient 7 en calculant l'expression `(d * e) % phi` pour d variant de 2 à 7. Commentez le rôle de la boucle `for`.

c) Les clés **publique** et **privée** sont elles **identiques** ou **différentes** ? Commentez votre réponse.

### 3.2) Chiffrement et déchiffrement

```python
# Message à chiffrer (maxi: n-1)
message = 5

# Chiffrement : c = m^e mod n
chif = pow(message, e, n)

# Déchiffrement : m = c^d mod n
dechif = pow(chif, d, n)
```

> _Rappel :_
> La fonction `pow(a, b, c)` en Python retourne : a<sup>b</sup>  mod c
> 
> Autrement dit, elle calcule la **puissance de `a` à l’exposant `b`**, puis **prend le reste de la division par `c`**.
> 
> Exemple : `pow(2, 5, 13)  # Résultat : 6`
> 
> En effet : 2<sup>5</sup> = 32 et 32 mod 13 = 6

3.2.1) Calculez `chif`

3.2.2) Calculez `dechif`

3.2.3) pourquoi `dechif` a la même valeur que **le message original** ?

3.2.4) Que donnerait un déchiffrement avec la clé publique ? (justifiez et commentez)

## 4) Chiffrement affine

Chaque lettre (uniquement les majuscules) est représentée par un entier dans l'ordre alphabétique ('A' = 0, 'B' = 1, etc.)

Le chiffrement affine d'un entier **x** est défini par

E<sub>a,b</sub>​(**x**) =  [a·**x**+b ] mod 26

et le déchiffrement d'un entier **y** par

D<sub>a,b​</sub>(**y**) = [ a<sup>−1</sup> · (**y**−b) ] mod 26,

où a est "*inversible modulo 26*" (c’est–à–dire que **pgcd(a, 26) = 1** ).

### 4.1) Vérification de la clé

4.1.1) Pour chacune des valeurs suivantes, déterminer si a est inversible modulo 26. Justifier en calculant pgcd(a, 26) :

- a = 5

- a = 6

- a = 7

4.1.2) Parmi les trois couples (a, b) suivants, lesquels peuvent définir un chiffrement affine valide ?

- (5, 8)

- (6, 3)

- (7, 15)

### 4.2) Chiffrement et déchiffrement

On choisit la clé (a, b) = (5, 8), qui est valide puisque pgcd(5, 26)=1.

#### 4.2.1) Chiffrement

Chiffrer le mot « CASSIS » (justifiez uniquement le chiffrement du 'C').

#### 4.2.2) Déchiffrement

4.2.2.1) Vérifiez que a<sup>-1</sup> = 21

4.2.2.2) déchiffrer la chaîne « VUW ». (justifiez uniquement le déchiffrement du 'V').

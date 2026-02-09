# Introduction à la cryptographie

## Résumé de cours

> Voir la page web [Pixees](https://informatique-lycee.forge.apps.education.fr/terminale_nsi/cours-terminale/c12c/)

> Voir la page web [Lycée Saint-Aspais](https://mcoilhac.forge.apps.education.fr/term/cryptographie/1_securite_comm/#decouverte)


## Synthèse

1. Donnez les différences entre chiffrement **symétrique** et **asymétrique**
2. Expliquez les termes **clé publique** et **clé privée**
3. Résumez en quelques lignes le principe du protocole *HTTPS*.

## Exercices

### Chiffrage et déchiffrage *XOR*

#### Exercice 1

Chiffrez la suite de bits `S` avec la clé `C` (qui sera répétée jusqu'à la longueur de S). On nommera `T` la suite binaire résulante:
 - S = `1001010011010110001010`
 - C = `1001101`

Déchiffrez `T` et constatez que l'on retrouve bien `S`.

#### Exercice 2

Même problème, en code *ASCII* avec :
- S = `Bonjour`
- C = `kzu`

#### Exercice 3

Même problème en *UTF-8* avec :

- S = `π/2 ≠ 1` (attention : il y a deux espaces)
- C = `é€`

Bien entendu, `T` n'est pas de l'*UTF-8*. Vous l'exprimerez donc en **hexadécimal**

#### Exercice 4

Concevez une fonction *Python* qui prendra en paramètres deux **bytes** `S` et `C` et effectuera un chiffrement (ou dechiffrement) de type *XOR*.

#### Exercice 5

Comme l'exercice 4, mais la fonction "reconnaîtra" (utilisez`isinstance()`) le type de `S` :

- si `S` est du type `str`, alors la fonction **chiffrera** cette chaîne encodée en UTF-8 et retournera un type `bytes`
- si `S` est du type `bytes`, alors la fonction **déchiffrera** cette suite d'octets et retournera le résutat décodé (du type `str`)

`T` sera une chaîne *unicode* du type `str`

### Chiffrage et déchiffrage **asymétrique** type *RSA*

> Introduction : lire la [page *Wikipedia*](https://fr.wikipedia.org/wiki/Chiffrement_RSA)

#### Exercice 1

Après analyse du programme suivant :

```python
# Choix de petits nombres premiers p et q
p = 23
q = 61

# Calcul de n et de φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Choix d'un exposant e (doit être premier avec φ(n))
e = 17  

# Calcul de d (l'inverse modulaire de e modulo φ(n))
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

d = mod_inverse(e, phi)

# Clés générées
cle_pub = (e, n)
cle_priv = (d, n)

print(f'Clé publique: {cle_pub}')
print(f'Clé privée: {cle_priv}')

# Message à chiffrer (maxi: n-1)
message = 42  # Exemple: 42 en décimal
print(f'Message original: {message}')

# Chiffrement : c = m^e mod n
chif = pow(message, e, n)
print(f"Message chiffré : {chif}")

# Déchiffrement : m = c^d mod n
dechif = pow(chif, d, n)
print(f"Message déchiffré : {dechif}")
```

Vous choisirez d'autres valeurs pour `p`, `q`, `e` et `message` illustrant le fonctionnement du chiffrement *RSA*.

Vous décrirez en quelques lignes :
- la création des clés
- le chiffrement
- le déchiffrement

#### Exercice 2

On modifie ce programme de manière à :
- pouvoir chiffrer une chaîne *ASCII* d'au maximum 4 caractères
- calculer plus efficacement l'*inverse modulaire*

```python
# Choix de nombres premiers p et q pour chiffrer "~~~~"
p = 16381
q = 16411

# Calcul de n et de φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Choix de l'exposant e (doit être premier avec φ(n))
e = 65537  # Valeur courante pour RSA

# Algorithme d'Euclide étendu pour trouver l'inverse modulaire
def pgcd_etendu(a, b):
    if b == 0:
        return a, 1, 0
    else:
        pgcd, x1, y1 = pgcd_etendu(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return pgcd, x, y

def inverse_modulaire(e, phi):
    pgcd, x, _ = pgcd_etendu(e, phi)
    if pgcd != 1:
        raise Exception("L'inverse modulaire n'existe pas")
    else:
        return x % phi

d = inverse_modulaire(e, phi)

# Clés générées
cle_publique = (e, n)
cle_privee = (d, n)

print(f'Clé publique : {cle_publique}')
print(f'Clé privée : {cle_privee}')

# Message à chiffrer
message = "~~~~"  # La chaîne ASCII maximale sur 4 caractères
print(f'Message original : {message}')

# Calcul de la somme pondérée des codes ASCII
somme_ponderee = sum(ord(caractere) * (128 ** i) for i, caractere in enumerate(message))
print(f'Somme pondérée des codes ASCII : {somme_ponderee}')

# Vérification que n est bien supérieur à la somme pondérée
if somme_ponderee >= n:
    raise Exception("n n'est pas assez grand pour chiffrer le message.")

# Chiffrement de la somme pondérée
message_chiffre = pow(somme_ponderee, e, n)
print(f"Message chiffré : {message_chiffre}")

# Déchiffrement
somme_dechiffree = pow(message_chiffre, d, n)
print(f"Somme pondérée déchiffrée : {somme_dechiffree}")

# Reconstruction du message à partir de la somme pondérée déchiffrée
message_dechiffre = ""
reste = somme_dechiffree

while reste > 0:
    code_caractere = reste % 128
    message_dechiffre += chr(code_caractere)
    reste //= 128

print(f"Message déchiffré : {message_dechiffre}")
```
Testez ce programme avec le message `"TNSI"` puis avec `"ABCDE"`.

Que constatez-vous ? Justifiez les deux cas, en prenant en compte que ce programme a été testé avec `"~~~~"`.

Vous analyserez les modifications apportées, et surtout :
- à quoi correspond la variable `somme_pondérée` ?
- comment sont choisis `p` et `q` ?
- quel est l'utilité de l'*algorithme d'Euclide étendu* ?
- comment fonctionne le déchiffrement (boucle `while` en fin de programme) ?
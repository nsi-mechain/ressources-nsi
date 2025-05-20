# Choix de petits nombres premiers p et q
p = 3
q = 11

# Choix d'un exposant e (doit être premier avec φ(n))
e = 3

# Calcul de n et de φ(n)
n = p * q
phi = (p - 1) * (q - 1)
print(f'n: {n} et phi: {phi}')


# Calcul de d (l'inverse modulaire de e modulo φ(n))
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

d = mod_inverse(e, phi)
print(f'd: {d}')

# Clés générées
cle_pub = (e, n)
cle_priv = (d, n)

print(f'Clé publique : {cle_pub}')
print(f'Clé privée : {cle_priv}')

# Message à chiffrer (valeur maxi : n-1)
message = 5
print(f'Message original : {message}')

# Chiffrement : c = m^e mod n
chif = pow(message, e, n)
print(f"Message chiffré : {chif}")

# Déchiffrement : m = c^d mod n
dechif = pow(chif, d, n)
print(f"Message déchiffré : {dechif}")

import socket
import random
import math

# Cette fonction retourne True si l'argument est un nombre premier
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

# Cette fonction génère un nombre aléatoire puis vérifie s'il est premier.
# Si ce n'est pas le cas, elle recommence jusqu'à en trouver un.
def generer_premier(max_val=50):
    while True:
        p = random.randint(2, max_val)
        if est_premier(p):
            return p

# Renvoie le pgcd (Plus Grand Commun Diviseur) entre a et b
# grâce à l'algorithme d'Euclide.
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calcule l'inverse modulaire de e modulo phi.
# On cherche un nombre d tel que :
# (e * d) % phi == 1
# Ce sera la clé privée.
def inverse_modulaire(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d


# =========================
# Génération des clés RSA
# =========================

# Génération de deux nombres premiers distincts p et q
p = generer_premier()
q = generer_premier()

# On s'assure que p et q sont différents
while q == p:
    q = generer_premier()

# Calcul de n (module public)
n = p * q

# Calcul de phi(n) = (p-1)(q-1)
phi = (p - 1) * (q - 1)

# Choix de e :
# On cherche un nombre premier avec phi (pgcd(e, phi) == 1)
# Cela permet de faire l'inverse modulaire
for e in range(2, phi):
    if pgcd(e, phi) == 1:
        break

# Calcul de d (clé privée) comme inverse modulaire de e modulo phi
d = inverse_modulaire(e, phi)

# =========================
# Partie réseau (Alice)
# =========================

# Création d'un socket TCP
s = socket.socket()

# Le serveur écoute sur toutes les interfaces réseau au port 5067
s.bind(("0.0.0.0", 5067))

# Mise en attente de connexions
s.listen()

print("Alice attend une connexion...")

# Acceptation d'une connexion entrante
conn, addr = s.accept()
print("Connecté à :", addr)

# Envoi de la clé publique (e, n) au client
# Format : "e,n"
conn.send(f"{e},{n}".encode())

# Réception du message chiffré envoyé par le client
data = conn.recv(1024).decode()
c = int(data)  # Conversion en entier

# Déchiffrement avec la clé privée :
# m = c^d mod n
m = pow(c, d, n)

print("Message chiffré reçu :", c)
print("Message déchiffré :", m)

# Fermeture de la connexion
conn.close()
s.close()

# maid-made

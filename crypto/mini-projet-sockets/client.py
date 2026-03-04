import socket

# Un socket est un connecteur, ici vers le réseau. il se définit par une adresse IP et un port. 
# C'est une interface prévisible pour envoyer et recevoir des données (des octets bruts). Le client et le serveur ont chacun un socket différent
# 
# Mais un socket peut aussi servir sans réseau, comme pour de la communication inter-processus (il se définit alors par un chemin de fichier)
#
# Il peut etre utilisé en mode connecté (TCP) ou en mode non connecté (UDP)
#
# Les sockets s'utilisent comme des fichiers (méthodes read et write), ainsi les programmeurs connaissent déja

# message secret
secret = 67


s = socket.socket()
s.connect((input("rentrez l'adresse du serveur : "), 5067))
print("connected")
pubkey=s.recv(1024).decode() #on recoit la clé publique sous la forme "e,n"

e,n = (int(a)for a in pubkey.split(',')) # on convertis le format "e,n" en deux nombres


ciphered = pow(secret,e,n) # chiffrement RSA a l'aide de l'exponentiation modulaire


s.send(str(ciphered).encode()) # on envoie le message converti en string et encodé pour le réseau
print("sent,",ciphered)
s.close() # on ferme la connection

#1: la couche de chiffrement (RSA)

#2: le format des données : string encodées puis décodées pour le réseau

#3: la couche réseau : les sockets

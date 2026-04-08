# Projet NSI – RSA sur réseau local (trinôme)

## Principe du projet

Vous allez simuler une communication chiffrée sur un réseau local à l’aide de **RSA**.

Chaque trinôme est composé de :

* **Alice** : génère les clés et reçoit les messages
* **Paul** : chiffre un message et l’envoie
* **Pirate** : intercepte la transmission et tente de casser le chiffrement

Le but est de comprendre **comment fonctionne RSA** et **pourquoi il faut de grands nombres pour être sécurisé**.

---

## Contraintes

* Message : entier entre **2 et 99**
* Nombres premiers : **≤ 50**
* Python sous Linux
* Communication via **sockets réseau**
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

# Travail à réaliser

## 1. Alice (serveur)

Créer un programme qui :

* choisit p et q
* calcule les clés RSA
* envoie la clé publique à Paul
* reçoit un message chiffré
* le déchiffre

---

## 2. Paul (client)

Créer un programme qui :

* se connecte à Alice
* reçoit la clé publique
* choisit un message
* le chiffre
* l’envoie

---

## 3. Pirate (attaque)

Créer un programme qui :

* récupère (e, n) et le message chiffré
* factorise n
* retrouve la clé privée
* déchiffre le message

---

## Méthode d’attaque

Le pirate doit tester tous les diviseurs possibles :

```
pour i de 2 à n :
    si n % i == 0 :
        p = i
        q = n // i
```

Puis reconstruire la clé privée.

---

# Conseils pour la communication réseau (sockets Python)

## Principe client / serveur

* **Alice = serveur**
* **Paul = client**
* Alice doit être lancée **avant** Paul

---

## Exemple minimal : serveur (Alice)

```
import socket

s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen()

conn, addr = s.accept()
data = conn.recv(1024).decode()

conn.send("message reçu".encode())
conn.close()
```

---

## Exemple minimal : client (Paul)

```
import socket

s = socket.socket()
s.connect(("IP_ALICE", 5000))

s.send("bonjour".encode())
reponse = s.recv(1024).decode()

s.close()
```

---

## Conseils pratiques

* Remplacer `IP_ALICE` par l’adresse IP d’Alice
* Utiliser des messages texte simples :

```
"e;n;c"
```

* Convertir avec :

```
str(x) / int(x)
encode() / decode()
```

* Toujours fermer la connexion avec `close()`
* Tester d’abord avec des messages simples

---

# Livrables

Votre groupe doit rendre :

* les 3 programmes Python
* un court texte expliquant :

  * comment fonctionne RSA
  * comment le pirate casse la clé
  * pourquoi RSA réel est sûr

---

# Questions à discuter

* L’attaque est-elle rapide ?
* Que se passe-t-il si on augmente la taille des nombres ?
* Comment améliorer la sécurité ?

---

## Bonus (facultatif)

* Ajouter un padding simple
* Envoyer plusieurs messages
* Mesurer le temps d’attaque

def factoriser_n(n):
    """Retourne p et q tels que n = p * q"""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None


def calculer_d(e, phi):
    """Trouve d tel que e*d ≡ 1 mod phi"""
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


def bruteforce_rsa():
    print("=== Attaque RSA ===")
    
    # 🔑 Entrée clé publique
    n = int(input("Entrez n : "))
    e = int(input("Entrez e : "))
    
    # 🧩 Factorisation
    print("\nFactorisation de n...")
    p, q = factoriser_n(n)
    
    if p is None:
        print("Impossible de factoriser n.")
        return
    
    print("p =", p)
    print("q =", q)
    
    # 🧮 Calcul phi
    phi = (p - 1) * (q - 1)
    print("phi(n) =", phi)
    
    # 🔓 Calcul clé privée
    print("\nRecherche de la clé privée...")
    d = calculer_d(e, phi)
    
    if d is None:
        print("Impossible de trouver d.")
        return
    
    print("Clé privée trouvée !")
    print("d =", d)
    
    # 📩 Déchiffrement optionnel
    while True:
        choix = input("\nVoulez-vous déchiffrer un message ? (o/n) : ")
        
        if choix.lower() == "o":
            c = int(input("Entrez le message chiffré (nombre) : "))
            m = pow(c, d, n)
            print("Message déchiffré (nombre) :", m)
            
            try:
                print("Message ASCII :", chr(m))
            except:
                print("Impossible de convertir en caractère.")
        
        elif choix.lower() == "n":
            print("Fin du programme.")
            break
        
        else:
            print("Réponse invalide.")


# Lancer le programme
bruteforce_rsa()

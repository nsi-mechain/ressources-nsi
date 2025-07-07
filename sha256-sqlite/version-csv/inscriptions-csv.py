import csv
import hashlib
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "utilisateurs.csv")

def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_users():
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_users(users):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["pseudo", "sha256", "inscription", "chpasswd"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def inscrire():
    users = read_users()
    pseudo = input("Choisissez un nom d'utilisateur : ")
    if any(u["pseudo"] == pseudo for u in users):
        print("Ce nom d'utilisateur existe déjà.")
        return
    mdp = input("Choisissez un mot de passe : ")
    hash_mdp = sha256_hash(mdp)
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    users.append({
        "pseudo": pseudo,
        "sha256": hash_mdp,
        "inscription": now,
        "chpasswd": now
    })
    write_users(users)
    print("Inscription réussie !")

def se_connecter():
    users = read_users()
    pseudo = input("Nom d'utilisateur : ")
    mdp = input("Mot de passe : ")
    hash_mdp = sha256_hash(mdp)
    for u in users:
        if u["pseudo"] == pseudo and u["sha256"] == hash_mdp:
            print("Connexion réussie !")
            return
    print("Échec de la connexion (identifiants incorrects).")

def changer_mdp():
    users = read_users()
    pseudo = input("Nom d'utilisateur : ")
    ancien_mdp = input("Ancien mot de passe : ")
    hash_ancien = sha256_hash(ancien_mdp)
    for u in users:
        if u["pseudo"] == pseudo and u["sha256"] == hash_ancien:
            nouveau_mdp = input("Nouveau mot de passe : ")
            hash_nouveau = sha256_hash(nouveau_mdp)
            u["sha256"] = hash_nouveau
            from datetime import datetime
            u["chpasswd"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_users(users)
            print("Mot de passe modifié avec succès !")
            return
    print("Ancien mot de passe incorrect.")

def se_desinscrire():
    users = read_users()
    pseudo = input("Nom d'utilisateur à supprimer : ")
    mdp = input("Mot de passe : ")
    hash_mdp = sha256_hash(mdp)
    for i, u in enumerate(users):
        if u["pseudo"] == pseudo and u["sha256"] == hash_mdp:
            del users[i]
            write_users(users)
            print("Utilisateur supprimé.")
            return
    print("Identifiants incorrects.")

def main():
    print("Menu :\n1) Se connecter\n2) S'inscrire\n3) Changer le mot de passe\n4) Se désinscrire")
    choix = input("Votre choix (1/2/3/4) : ")
    if choix == "1":
        se_connecter()
    elif choix == "2":
        inscrire()
    elif choix == "3":
        changer_mdp()
    elif choix == "4":
        se_desinscrire()
    else:
        print("Choix invalide.")

    print("Au revoir.")

if __name__ == "__main__":
    main()

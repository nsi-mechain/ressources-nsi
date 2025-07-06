import sqlite3
import hashlib
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "utilisateurs.db")

def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS liste_utilisateurs (
                pseudo TEXT PRIMARY KEY,
                sha256 TEXT,
                inscription TEXT,
                chpasswd TEXT
            )
        """)
        conn.commit()

def inscrire():
    pseudo = input("Choisissez un nom d'utilisateur : ")
    mdp = input("Choisissez un mot de passe : ")
    hash_mdp = sha256_hash(mdp)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM liste_utilisateurs WHERE pseudo = ?", (pseudo,))
        if c.fetchone():
            print("Ce nom d'utilisateur existe déjà.")
            return
        c.execute(
            "INSERT INTO liste_utilisateurs (pseudo, sha256, inscription, chpasswd) "
            "VALUES (?, ?, datetime('now','localtime'), datetime('now','localtime'))",
            (pseudo, hash_mdp)
        )
        conn.commit()
        print("Inscription réussie !")

def se_connecter():
    pseudo = input("Nom d'utilisateur : ")
    mdp = input("Mot de passe : ")
    hash_mdp = sha256_hash(mdp)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM liste_utilisateurs WHERE pseudo = ? AND sha256 = ?", (pseudo, hash_mdp))
        if c.fetchone():
            print("Connexion réussie !")
        else:
            print("Échec de la connexion (identifiants incorrects).")

def changer_mdp():
    pseudo = input("Nom d'utilisateur : ")
    ancien_mdp = input("Ancien mot de passe : ")
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM liste_utilisateurs WHERE pseudo = ? AND sha256 = ?", (pseudo, sha256_hash(ancien_mdp)))
        if c.fetchone():
            nouveau_mdp = input("Nouveau mot de passe : ")
            hash_nouveau = sha256_hash(nouveau_mdp)
            c.execute(
                "UPDATE liste_utilisateurs SET sha256 = ?, chpasswd = datetime('now','localtime') WHERE pseudo = ?",
                (hash_nouveau, pseudo)
            )
            conn.commit()
            print("Mot de passe modifié avec succès !")
        else:
            print("Ancien mot de passe incorrect.")

def se_desinscrire():
    pseudo = input("Nom d'utilisateur à supprimer : ")
    mdp = input("Mot de passe : ")
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM liste_utilisateurs WHERE pseudo = ? AND sha256 = ?", (pseudo, sha256_hash(mdp)))
        if c.fetchone():
            c.execute("DELETE FROM liste_utilisateurs WHERE pseudo = ?", (pseudo,))
            conn.commit()
            print("Utilisateur supprimé.")
        else:
            print("Identifiants incorrects.")

def main():
    create_db()
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
2

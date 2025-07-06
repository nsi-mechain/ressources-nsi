# Gestion d'utilisateurs avec SHA-256 et SQLite

## Description du projet

Ce projet propose un petit programme Python permettant de gérer une liste d’utilisateurs à l’aide d’une base de données SQLite. Chaque utilisateur dispose d’un nom d’utilisateur (pseudo) et d’un mot de passe, stocké sous forme de hachage (SHA-256) pour garantir la sécurité. Les utilisateurs peuvent :

- S’inscrire
- Se connecter
- Changer leur mot de passe
- Se désinscrire (supprimer leur compte)

Les dates d’inscription et de dernière modification du mot de passe sont également enregistrées, le tout dans un fichier `utilisateurs.db` créé automatiquement.

## Le rôle du hachage des mots de passe

Un mot de passe ne doit jamais être stocké en clair dans une base de données. À la place, on stocke son **empreinte** (ou "hash"), c’est-à-dire le résultat d’une fonction mathématique (ici SHA-256) qui transforme le mot de passe en une chaîne incompréhensible, impossible à inverser. Ainsi, même si la base de données est compromise, les mots de passe réels restent protégés.

Lors de la connexion ou du changement de mot de passe, le mot de passe saisi est haché et comparé à la valeur enregistrée.

## Analyse des fonctions

### 1. `sha256_hash(password)`
- Reçoit un mot de passe en clair et retourne son empreinte SHA-256 sous forme de texte.

### 2. `create_db()`
- Crée la base de données et la table `liste_utilisateurs` si elle n’existe pas déjà. Les champs enregistrés sont :
    - pseudo : identifiant unique de l’utilisateur (clé primaire)
    - sha256 : mot de passe haché
    - inscription : date/heure d’inscription
    - chpasswd : date/heure du dernier changement de mot de passe

### 3. `inscrire()`
- Permet à un nouvel utilisateur de s’inscrire. Vérifie si le pseudo existe déjà. Hache le mot de passe et enregistre le tout dans la base, avec la date d’inscription et de changement de mot de passe (initialisée à maintenant).

### 4. `se_connecter()`
- Permet à un utilisateur existant de se connecter en vérifiant que le couple pseudo/mot de passe haché correspond à une entrée dans la base.

### 5. `changer_mdp()`
- Permet à un utilisateur de changer son mot de passe après vérification de l’ancien mot de passe. Met à jour le hachage et la date de changement de mot de passe.

### 6. `se_desinscrire()`
- Permet à un utilisateur de supprimer son compte après vérification du mot de passe.

### 7. `main()`
- Fonction principale du programme :
    - Crée la base si besoin
    - Affiche un menu pour choisir une action (connexion, inscription, changement de mot de passe, suppression de compte)
    - Exécute la fonction correspondante selon le choix de l’utilisateur

## À retenir
- **Aucun mot de passe n’est jamais stocké en clair.**
- La gestion de la base de données est entièrement automatique.
- Le hachage SHA-256 n’est pas réversible : il est impossible de retrouver le mot de passe à partir du hachage seul.
- Ce programme est un exemple didactique : il ne gère pas toutes les situations réelles (ex : politique de mot de passe, sécurité contre les attaques par force brute, etc.)

---

**À tester :**
- Inscription, connexion, changement de mot de passe, suppression de compte
- Observez le fichier `utilisateurs.db` avec un logiciel SQLite si besoin




---

# Initiation à SQLite

---

## 1. **Qu’est-ce que SQLite ?**

- **SQLite** est un système de gestion de bases de données relationnelles (SGBDR).

- Il se distingue par sa **simplicité** : pas besoin de serveur séparé, la base de données tient dans un **fichier unique**.

- Très utilisé dans les applications mobiles, les navigateurs web, les objets connectés, etc.

**À retenir :**  
SQLite est une bibliothèque légère pour manipuler des bases de données facilement et localement.

---

## 2. **Pourquoi utiliser SQLite ?**

- Facile à installer : aucun service serveur à démarrer.

- Format portable : la base de données est un fichier (`.sqlite` ou `.db`).

- Suffisant pour des applications individuelles, des petits sites ou des prototypes.

- Idéal pour l’apprentissage de la programmation et du SQL.

---

## 3. **Concepts de base**

- **Base de données** : ensemble organisé de données stockées dans un fichier.

- **Table** : structure qui organise les données sous forme de lignes (enregistrements) et de colonnes (champs).

- **Champ/Colonne** : caractéristique d’une donnée (ex : nom, date).

- **Ligne/Enregistrement** : une donnée complète (ex : un élève).

---

## 4. **Types de données dans SQLite**

- `INTEGER` : nombre entier (ex : 3, 42)

- `REAL` : nombre décimal (ex : 3.14)

- `TEXT` : chaîne de caractères (ex : "Alice")

- `BLOB` : données binaires

- `NULL` : absence de valeur

---

## 5. **Utiliser SQLite : méthodes courantes**

### a) **Avec le terminal (ligne de commande)**

1. **Installation :**
   
   - Sous Linux : `sudo apt install sqlite3`
   
   - Sous Windows/Mac : Téléchargement sur [sqlite.org](https://sqlite.org/download.html)

2. **Création d’une base :**
   
   ```bash
   sqlite3 ma_base.sqlite
   ```
   
   → Cela ouvre l’invite de commandes SQLite sur le fichier (qui sera créé si besoin).

### b) **Avec Python**

- Bibliothèque standard `sqlite3` :
  
  ```python
  import sqlite3
  connexion = sqlite3.connect("ma_base.sqlite")
  curseur = connexion.cursor()
  ```

### c) **Avec un logiciel graphique**

- Exemples : [DB Browser for SQLite](https://sqlitebrowser.org/) (Windows/Linux/Mac).

---

## 6. **Premières manipulations en SQL**

Quelques commandes **basiques** à connaître (dans le terminal, un logiciel graphique ou Python) :

### a) **Créer une table**

```sql
CREATE TABLE eleves (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    age INTEGER
);
```

### b) **Insérer des données**

```sql
INSERT INTO eleves (nom, age) VALUES ('Alice', 17);
INSERT INTO eleves (nom, age) VALUES ('Bob', 18);
```

### c) **Afficher toutes les données**

```sql
SELECT * FROM eleves;
```

### d) **Rechercher un élève**

```sql
SELECT * FROM eleves WHERE nom = 'Alice';
```

### e) **Mettre à jour une donnée**

```sql
UPDATE eleves SET age = 18 WHERE nom = 'Alice';
```

### f) **Supprimer un élève**

```sql
DELETE FROM eleves WHERE nom = 'Bob';
```

---

## 7. **Bonnes pratiques et limites**

- **Faites des sauvegardes** régulières du fichier `.sqlite`.

- SQLite n’est pas adapté pour des applications à très fort trafic ou multi-utilisateurs en écriture simultanée.

- Idéal pour l’apprentissage, les petits projets, ou stocker des données localement.

---

## 8. **Ressources complémentaires**

- [Site officiel SQLite](https://sqlite.org/)

- [Tutoriel SQLite en français](https://openclassrooms.com/fr/courses/4425111-initiez-vous-a-sql-avec-mysql/4452436-decouvrez-les-bases-de-donnees)

- [DB Browser for SQLite](https://sqlitebrowser.org/)

---

### **Résumé**

- SQLite = SGBD léger et portable, facile à utiliser

- Manipulation de bases via terminal, Python ou logiciels graphiques

- Syntaxe SQL standard, adaptée à la découverte des bases de données relationnelles



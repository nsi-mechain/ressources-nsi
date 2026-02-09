# ✅ Fiche : INNER JOIN (ou simplement JOIN)

## 1. Définition

`INNER JOIN` permet de **lier deux tables** en ne conservant que les lignes **qui correspondent dans les deux tables**.

👉 Si aucune correspondance n’est trouvée, la ligne **n’apparaît pas** dans le résultat.

---

## 2. Syntaxe

```sql
SELECT colonnes
FROM table1
INNER JOIN table2
    ON table1.cle = table2.cle;
```

> Remarque : `JOIN` tout seul est **équivalent** à `INNER JOIN`.

Exemple strictement équivalent :

```sql
SELECT *
FROM table1
JOIN table2 ON table1.id = table2.id;
```

---

## 3. Exemple concret

### Table `Clients`

| id_client | nom     |
|-----------|----------|
| 1         | Alice    |
| 2         | Bob      |
| 3         | Charlie  |

### Table `Commandes`

| id_commande | id_client | montant |
|-------------|-----------|----------|
| 101         | 1         | 50 €     |
| 102         | 1         | 25 €     |
| 103         | 3         | 75 €     |

### Requête INNER JOIN

```sql
SELECT Clients.nom, Commandes.montant
FROM Clients
INNER JOIN Commandes
    ON Clients.id_client = Commandes.id_client;
```

### Résultat

| nom     | montant |
|---------|----------|
| Alice   | 50 €     |
| Alice   | 25 €     |
| Charlie | 75 €     |

👉 Bob n’apparaît pas car **il n’a pas de commande**.

---

## 4. À retenir

| JOIN utilisé | Résultat |
|--------------|----------|
| `JOIN` ou `INNER JOIN` | Uniquement les lignes qui correspondent dans les deux tables |

🧠 **Astuce :** INNER JOIN = intersection (comme en maths)

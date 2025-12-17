# Tutoriel pour le contrôle

Exemple d'utilisation de `sqlite3` pour créer une base de données (à une seule table), puis y effectuer des modifications en affichant à chaque fois la table.

## Première étape :
On crée le fichier `exemple.sql` suivant :

```SQL
.mode box

--1
.print "Création de la table matable :"
CREATE TABLE matable (Id INTEGER NOT NULL,
                      Nom TEXT,
                      age INTEGER,
                      PRIMARY KEY (Id));
INSERT INTO matable (Nom, age) VALUES
    ('toto', 16),
    ('tata', 12),
    ('titi', 29);
SELECT * FROM matable;

--2
.print "On change l'âge de tata :"
UPDATE matable SET age = 13 WHERE Nom LIKE 'tata';
SELECT * FROM matable;

--3
.print "On retire l'enregistrement titi:"
DELETE from matable WHERE Nom LIKE 'titi';
SELECT * FROM matable;
```

*Attention* : ce fichier mixe en fait des commandes **SQL** et des commandes **internes à sqlite3** (`.mode` et `.print`).

## Résultat obtenu après lancement de sqlite3, puis de la commande interne "`.read exemple.sql`" :

```text
Création de la table matable :
┌────┬──────┬─────┐
│ Id │ Nom  │ age │
├────┼──────┼─────┤
│ 1  │ toto │ 16  │
│ 2  │ tata │ 12  │
│ 3  │ titi │ 29  │
└────┴──────┴─────┘
On change l'âge de tata :
┌────┬──────┬─────┐
│ Id │ Nom  │ age │
├────┼──────┼─────┤
│ 1  │ toto │ 16  │
│ 2  │ tata │ 13  │
│ 3  │ titi │ 29  │
└────┴──────┴─────┘
On retire l'enregistrement titi:
┌────┬──────┬─────┐
│ Id │ Nom  │ age │
├────┼──────┼─────┤
│ 1  │ toto │ 16  │
│ 2  │ tata │ 13  │
└────┴──────┴─────┘
```
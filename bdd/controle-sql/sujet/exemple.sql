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
UPDATE matable
SET age = 13 WHERE Nom LIKE 'tata';
SELECT * FROM matable;

--3
.print "On retire l'enregistrement titi:"
DELETE from matable WHERE Nom LIKE 'titi';
SELECT * FROM matable;

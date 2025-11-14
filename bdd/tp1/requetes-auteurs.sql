--1
SELECT * FROM AUTEURS;

--2
SELECT nom, prenom FROM AUTEURS;

--3
SELECT DISTINCT langue_ecriture FROM AUTEURS;

--4
SELECT nom, naissance FROM AUTEURS WHERE naissance > 1900;

--5
SELECT nom FROM AUTEURS WHERE naissance = 1920 ORDER BY nom;

--6
SELECT nom, prenom FROM AUTEURS Where mort < 1990 ORDER BY nom ASC;

--7
SELECT nom FROM AUTEURS WHERE langue_ecriture = "français" AND naissance > 1900;

--8
SELECT nom, prenom, mort-naissance FROM AUTEURS Where mort-naissance<75 ORDER BY mort-naissance;

--9
UPDATE AUTEURS SET mort=1910 WHERE nom = 'Renard';
SELECT * FROM AUTEURS;

--10
DELETE FROM AUTEURS WHERE nom LIKE 'B%';
SELECT * FROM AUTEURS;

.mode box
.echo on

--2
SELECT titre FROM livre WHERE titre LIKE '%Astérix%';

--3
SELECT titre, annee AS année FROM livre WHERE titre LIKE '%Astérix%' AND editeur LIKE '%Dargaud%';

--4
SELECT titre, annee AS année FROM livre WHERE titre LIKE '%Astérix%' AND editeur LIKE '%Dargaud%' ORDER BY annee;

--5
SELECT titre FROM livre WHERE editeur LIKE '%Laffont%' AND annee > 2015;

--6
SELECT COUNT(*) AS nombre FROM livre WHERE annee BETWEEN 1995 AND 2000;

--7
SELECT titre, isbn, annee AS année FROM livre WHERE editeur LIKE '%Dargaud%' ORDER BY annee ASC LIMIT 1;

--8
SELECT DISTINCT editeur AS éditeur FROM livre WHERE annee < 1980 ORDER BY UPPER(editeur);

--9
SELECT
    '978-2218972324' AS ISBN,
    IIF ((SELECT editeur FROM livre WHERE isbn = '978-2218972324') = 'Hatier', 'oui', 'non') AS 'chez Hatier';

SELECT
    '978-2218972325' AS ISBN,
    IIF ((SELECT editeur FROM livre WHERE isbn = '978-2218972325') = 'Hatier', 'oui', 'non') AS 'chez Hatier';

--10
SELECT
    editeur AS éditeur,
    COUNT(*) as nombre FROM livre GROUP BY editeur HAVING nombre >= 3 ORDER BY nombre;

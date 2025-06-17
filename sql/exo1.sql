.mode box
.echo on


--1
CREATE TABLE trimestre2 (Id INTEGER PRIMARY KEY,
                         Nom TEXT,
                         Maths INTEGER,
                         Anglais INTEGER,
                         NSI INTEGER);
.tables

--2
INSERT INTO trimestre2 (Nom, Maths, Anglais, NSI) VALUES
    ('Alice', 16, 11, 17),
    ('Bob', 12, 15, 10),
    ('Charles', 9, 11, 18);

SELECT * FROM trimestre2;

--3
UPDATE trimestre2
SET Maths = 18 WHERE Nom LIKE 'Alice';

SELECT * FROM trimestre2;

--4
DELETE from trimestre2 WHERE Nom LIKE 'Bob';
SELECT * FROM trimestre2;

--5
INSERT INTO trimestre2 (Nom) VALUES ('Roger');

SELECT * FROM trimestre2;

--6
ALTER TABLE trimestre2 ADD SVT INTEGER;

SELECT * FROM trimestre2;

--7
UPDATE trimestre2 SET SVT = 15 WHERE Nom LIKE 'Alice';
UPDATE trimestre2 SET SVT = 12 WHERE Nom LIKE 'Charles';
UPDATE trimestre2 SET SVT = 17 WHERE Nom LIKE 'Roger';

SELECT * FROM trimestre2;

--8
DROP TABLE trimestre2;
.tables


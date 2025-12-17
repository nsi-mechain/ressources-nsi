CREATE TABLE AUTEURS
(id INT, nom TEXT, prenom TEXT, naissance INT, mort INT, langue_ecriture TEXT, PRIMARY KEY (id));

INSERT INTO AUTEURS
(id, nom, prenom, naissance, mort, langue_ecriture)
VALUES
(1,'Orwell','George',1903,1950,'anglais'),
(2,'Herbert','Frank',1920,1986,'anglais'),
(3,'Asimov','Isaac',1920,1992,'anglais'),
(4,'Huxley','Aldous',1894,1963,'anglais'),
(5,'Bradbury','Ray',1920,2012,'anglais'),
(6,'Renard','Jules',1864,1911,'français'),
(7,'Barjavel','René',1911,1985,'français'),
(8,'Boulle','Pierre',1912,1994,'français'),
(9,'Verne','Jules',1828,1905,'français');

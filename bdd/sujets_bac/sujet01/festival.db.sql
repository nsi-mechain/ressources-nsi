CREATE TABLE IF NOT EXISTS "concerts" (
	"idconc"	INTEGER,
	"scene"	INTEGER,
	"heure_debut"	TEXT,
	"heure_fin"	TEXT,
	"idgrp"	INTEGER,
	PRIMARY KEY("idconc"),
	FOREIGN KEY("idgrp") REFERENCES "groupes"("idgrp"),
	FOREIGN KEY("scene") REFERENCES "scenes"("id")
);
CREATE TABLE IF NOT EXISTS "groupes" (
	"idgrp"	INTEGER,
	"nom"	TEXT,
	"style"	TEXT,
	"nb_pers"	INTEGER,
	PRIMARY KEY("idgrp")
);
CREATE TABLE IF NOT EXISTS "musiciens" (
	"idmus"	INTEGER,
	"nom"	TEXT,
	"prenom"	TEXT,
	"instru"	TEXT,
	"idgrp"	INTEGER,
	PRIMARY KEY("idmus"),
	FOREIGN KEY("idgrp") REFERENCES "groupes"("idgrp")
);
CREATE TABLE IF NOT EXISTS "scenes" (
	"id"	INTEGER,
	"nom"	TEXT,
	"maxspectateurs"	INTEGER,
	"surface"	INTEGER,
	PRIMARY KEY("id")
);
INSERT INTO "concerts" VALUES (10,1,'20h00','20h45',12),
 (24,2,'20h00','20h45',25),
 (36,1,'21h00','22h00',96),
 (45,3,'18h00','18h30',87);
INSERT INTO "groupes" VALUES (12,'Weather Report','Latin Jazz',5),
 (25,'Breckers Brothersd','Swing Jazz',4),
 (87,'Return to Forever','Latin Jazz',8),
 (96,'The Jazz Messenger
','Free Jazz',3);
INSERT INTO "musiciens" VALUES (12,'Parker','Charlie','trompette',96),
 (13,'Parker','Charlie','trombone',25),
 (58,'Dufler','Candy','saxophone',96),
 (97,'Miles','Davis','saxophone',87);
INSERT INTO "scenes" VALUES (1,'Hendrix',200,100),
 (2,'Baez',500,250),
 (3,'Zappa',300,150);

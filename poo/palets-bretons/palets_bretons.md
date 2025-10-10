# Programmation Orientée Objet (POO)

## Mini-projet “Palets bretons”

![palets](https://www.gourmandiseries.fr/wp-content/uploads/2013/07/palet-breton-150x150.jpg)

### Partie 1 : POO à partir d’un programme *procédural*

Adaptez le code suivant de manière à ce que le “palet” traversant le “terrain” soit une instance d’une classe `Palet`.

```python
import pygame, time, sys

L = 800
H = 600
pygame.init()
terrain = pygame.display.set_mode((L, H))

# Caractéristiques du palet
x = 0
y = 0
vx = 1
vy = 1
rayon = 40
couleur = (255, 0, 0)

while True:
    terrain.fill([0, 64, 0])
    pygame.draw.circle(terrain, couleur, (x, y), rayon)

    x += vx
    y += vy  # le palet se déplace

    pygame.display.update()  # on redessine

    # fermeture de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    time.sleep(0.01)  # un petit délai
```

Cette classe contiendra :
- 3 attributs : `x`, `y` et `couleur`
- 2 méthodes : `deplace` et `dessine`

Instanciez un deuxième palet (autre couleur, autre point de départ, autres direction et vitesse) sans gérer une éventuelle “collision”.

### Partie 2 : collisions sur les murs

Il faudra modifier la méthode `deplace` pour que les palets rebondissent contre les murs entourant le terrain.

### Partie 3 : collisions entre palets

On donne le code de la fonction permettant d’obtenir les vitesses **après** collision entre deux palets :

```python
def apres_collision(x1, y1, vx1, vy1, x2, y2, vx2, vy2):
    """ calcule la vitesse de deux palets p1 et p2 après la collision
        renvoie le tuple (vx1', vy1', vx2', vy2')
    """
    def scalaire(x1, y1, x2, y2):
        return x1*x2 + y1*y2

    d = scalaire(x1-x2, y1-y2, x1-x2, y1-y2)   # carré de la distance M1M2
    ps = scalaire(vx1-vx2, vy1-vy2, x1-x2, y1-y2)  # produit scalaire des vecteurs v1-v2 et M1M2
    ux1 = vx1 - ps / d * (x1-x2)
    uy1 = vy1 - ps / d * (y1-y2)
    ux2 = vx2 - ps / d * (x2-x1)
    uy2 = vy2 - ps / d * (y2-y1)

    return ux1, uy1, ux2, uy2
```

Modifiez à nouveau la méthode `deplace`.

**Attention** : Dans cette partie, on définira une liste `jeu` qui contiendra l’ensemble des palets (des instances de la classe `Palet`) présents sur le terrain.

### Partie 4 : pour aller plus loin…

#### Utilisation d’une base de données :

Les palets du jeu seront définis dans une base de données *SQLite*. Vous pouvez vous inspirer du “dump SQL” suivant :

```sql
CREATE TABLE IF NOT EXISTS "couleurs" (
	"nom"	TEXT,
	"R"	INTEGER,
	"V"	INTEGER,
	"B"	INTEGER,
	PRIMARY KEY("nom")
);
INSERT INTO couleurs VALUES('cyan',100,255,100);
INSERT INTO couleurs VALUES('rouge',255,0,0);
INSERT INTO couleurs VALUES('citron',255,255,0);
INSERT INTO couleurs VALUES('blanc',255,255,255);
INSERT INTO couleurs VALUES('magenta',255,0,255);

CREATE TABLE IF NOT EXISTS "palets" (
	"id"	INTEGER NOT NULL UNIQUE,
	"x"	REAL,
	"y"	REAL,
	"vx"	REAL,
	"vy"	REAL,
	"couleur"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("couleur") REFERENCES "couleurs"("nom")
);
INSERT INTO palets VALUES(1,100.0,100.0,1.0,2.0,'cyan');
INSERT INTO palets VALUES(2,200.0,500.0,0.3,-1.5,'rouge');
INSERT INTO palets VALUES(3,500.0,200.0,0.1,0.4,'citron');
```

Votre programme devra extraire le jeu de palets avant d’exécuter l’animation.

#### Explosions :

Si, dans le jeu, des palets de couleurs identiques se rencontrent, alors ils “explosent” et disparaissent…


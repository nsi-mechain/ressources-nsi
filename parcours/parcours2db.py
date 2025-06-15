import sqlite3
import parcours
import math

def cap_rose_16(dx, dy):
    """
    Renvoie le cap en texte (rose des 16) pour un déplacement (dx, dy),
    repère centré, x droite = Est, y haut = Nord.
    """
    if dx == 0 and dy == 0:
        return None
    angle = (math.degrees(math.atan2(dy, dx)) + 360) % 360
    directions = [
        "E", "ENE", "NE", "NNE", "N", "NNO", "NO", "ONO",
        "O", "OSO", "SO", "SSO", "S", "SSE", "SE", "ESE"
    ]
    index = int((angle + 11.25) // 22.5) % 16
    return directions[index]




def distance(x0, y0, x1, y1):
    return math.hypot(x1 - x0, y1 - y0)

def main():
    # Lecture des points décodés
    points = parcours.lire_parcours("parcours_souris.bin")

    # Connexion à la base SQLite et création de la table
    conn = sqlite3.connect("parcours.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS points (
            id INTEGER PRIMARY KEY,
            x INTEGER,
            y INTEGER,
            cap TEXT,
            distance REAL
        )
    """)
    c.execute("DELETE FROM points")  # Pour écraser un éventuel ancien contenu

    for i, (x, y) in enumerate(points):
        if i < len(points) - 1:
            x_suiv, y_suiv = points[i+1]
            dx = x_suiv - x
            dy = y_suiv - y
            cap = cap_rose_16(dx, dy)
            dist = distance(x, y, x_suiv, y_suiv)
        else:
            cap = None
            dist = None
        c.execute(
            "INSERT INTO points (id, x, y, cap, distance) VALUES (?, ?, ?, ?, ?)",
            (i + 1, x, y, cap, dist)
        )

    conn.commit()
    conn.close()
    print("Base de données parcours.db créée.")

if __name__ == "__main__":
    main()

import zlib

def int_to_11bits(n):
    """Convertit un entier signé (-1024 à +1023) en entier non signé sur 11 bits (0 à 2047)."""
    if not -1024 <= n <= 1023:
        raise ValueError("n doit être compris entre -1024 et +1023")
    return n % 2048

def bits11_to_int(n):
    """Convertit un entier non signé sur 11 bits (0 à 2047) en entier signé (-1024 à +1023)."""
    if n >= 1024:
        return n - 2048
    else:
        return n

def empaqueter_2x11bits(a, b):
    """Empaqueter deux entiers (chacun sur 11 bits) en 22 bits (3 octets)."""
    v = (a << 11) | b  # 22 bits
    return bytes([(v >> 16) & 0xFF, (v >> 8) & 0xFF, v & 0xFF])

def desempaqueter_2x11bits(tranche):
    """Désempaqueter 3 octets en deux entiers sur 11 bits."""
    v = (tranche[0] << 16) | (tranche[1] << 8) | tranche[2]
    a = (v >> 11) & 0x7FF  # 11 bits
    b = v & 0x7FF
    return a, b

def en_differentiel(points):
    """Convertit une liste de points [(x, y), ...] en liste de déplacements différentiels [(dx, dy), ...]."""
    deplacements = []
    precedent = points[0]
    for point in points[1:]:
        dx = point[0] - precedent[0]
        dy = point[1] - precedent[1]
        deplacements.append((dx, dy))
        precedent = point
    return deplacements

def depuis_differentiel(depart, deplacements):
    """Reconstruit la liste de points à partir du point de départ et des déplacements différentiels."""
    points = [depart]
    for dx, dy in deplacements:
        x, y = points[-1]
        points.append((x + dx, y + dy))
    return points

def ecrire_parcours(nom_fichier, points):
    """Écrit un parcours compressé dans un fichier binaire, adapté au repère centré."""
    tampon = bytearray()
    # Point de départ sur 2x11 bits
    x0, y0 = points[0]
    tampon.extend(empaqueter_2x11bits(int_to_11bits(x0), int_to_11bits(y0)))
    # Chaque déplacement différentiel sur 2x11 bits
    for dx, dy in en_differentiel(points):
        tampon.extend(empaqueter_2x11bits(int_to_11bits(dx), int_to_11bits(dy)))
    # Compression avec zlib
    donnees = zlib.compress(bytes(tampon), 9)
    with open(nom_fichier, "wb") as f:
        f.write(donnees)

def lire_parcours(nom_fichier):
    """Lit et décompresse un parcours à partir d'un fichier binaire adapté au repère centré."""
    with open(nom_fichier, "rb") as f:
        donnees = zlib.decompress(f.read())
    n = len(donnees) // 3  # Nombre de paires (point de départ + déplacements)
    paires = [desempaqueter_2x11bits(donnees[3*i:3*i+3]) for i in range(n)]
    # Récupérer le point de départ
    x0, y0 = (bits11_to_int(paires[0][0]), bits11_to_int(paires[0][1]))
    # Récupérer les déplacements différentiels
    deplacements = [ (bits11_to_int(dx), bits11_to_int(dy)) for dx, dy in paires[1:] ]
    return depuis_differentiel((x0, y0), deplacements)

# Exemple d'utilisation
if __name__ == "__main__":
    parcours = [(0, 0), (10, 20), (15, 18), (10, 10), (-30, 40)]
    ecrire_parcours("parcours_centre.bin", parcours)
    lu = lire_parcours("parcours_centre.bin")
    print(lu)


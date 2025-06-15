import tkinter as tk
import parcours
import os
from PIL import Image, ImageDraw
import math

TAILLE_CANEVAS = 1024
CENTRE = TAILLE_CANEVAS // 2

def ecran_vers_repere(x_pixel, y_pixel):
    """Convertit les coordonnées pixel en coordonnées repère centré, y vers le haut."""
    x = x_pixel - CENTRE
    y = CENTRE - y_pixel
    return x, y

def repere_vers_ecran(x, y):
    """Convertit des coordonnées repère en coordonnées pixel (pour affichage sur canevas)."""
    x_pixel = x + CENTRE
    y_pixel = CENTRE - y
    return x_pixel, y_pixel

def enregistrer_clic(event):
    x, y = ecran_vers_repere(event.x, event.y)
    points.append((x, y))
    # Dessiner le point (reconverti)
    x_pixel, y_pixel = repere_vers_ecran(x, y)
    rayon = 3
    canevas.create_oval(x_pixel-rayon, y_pixel-rayon, x_pixel+rayon, y_pixel+rayon, fill="red")
    # Relier au point précédent si besoin
    if len(points) > 1:
        x0, y0 = points[-2]
        x0_pixel, y0_pixel = repere_vers_ecran(x0, y0)
        canevas.create_line(x0_pixel, y0_pixel, x_pixel, y_pixel, fill="blue")

def dessiner_fleche(draw, x0, y0, x1, y1, taille=32, couleur="green"):
    """Dessine une flèche centrée sur le segment [x0,y0]-[x1,y1], dans le sens du déplacement."""
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    dx = x1 - x0
    dy = y1 - y0
    if dx == 0 and dy == 0:
        return
    angle = math.atan2(dy, dx)  # y vers le haut
    px = mx + (taille / 2) * math.cos(angle)
    py = my + (taille / 2) * math.sin(angle)
    angle_aile = math.radians(25)
    l_aile = taille / 2.5
    aile1 = (
        px - l_aile * math.cos(angle - angle_aile),
        py - l_aile * math.sin(angle - angle_aile)
    )
    aile2 = (
        px - l_aile * math.cos(angle + angle_aile),
        py - l_aile * math.sin(angle + angle_aile)
    )
    # Conversion repère → pixel
    mx_pix, my_pix = repere_vers_ecran(mx, my)
    px_pix, py_pix = repere_vers_ecran(px, py)
    aile1_pix = repere_vers_ecran(*aile1)
    aile2_pix = repere_vers_ecran(*aile2)
    draw.line([ (mx_pix, my_pix), (px_pix, py_pix) ], fill=couleur, width=2)
    draw.line([ (px_pix, py_pix), aile1_pix ], fill=couleur, width=2)
    draw.line([ (px_pix, py_pix), aile2_pix ], fill=couleur, width=2)

def sauvegarder_png(nom_image, points):
    image = Image.new("RGB", (TAILLE_CANEVAS, TAILLE_CANEVAS), "white")
    draw = ImageDraw.Draw(image)
    # Tracer les lignes du parcours
    if len(points) > 1:
        lignes = [repere_vers_ecran(x, y) for (x, y) in points]
        draw.line(lignes, fill="blue", width=2)
    # Dessiner les points
    for x, y in points:
        x_pixel, y_pixel = repere_vers_ecran(x, y)
        r = 3
        draw.ellipse((x_pixel-r, y_pixel-r, x_pixel+r, y_pixel+r), fill="red", outline="red")
    # Flèches sur chaque segment
    for i in range(len(points)-1):
        x0, y0 = points[i]
        x1, y1 = points[i+1]
        dessiner_fleche(draw, x0, y0, x1, y1, taille=32, couleur="green")
    image.save(nom_image)

def fermer():
    racine.destroy()
    if not points:
        print("Aucun point n'a été enregistré.")
        return

    print("\nListe des points (repère centré, x droite, y haut) :")
    print(points)

    deplacements = parcours.en_differentiel(points)
    print("\nListe des déplacements :")
    print(deplacements)

    nom_fichier = "parcours_souris.bin"
    parcours.ecrire_parcours(nom_fichier, points)
    taille = os.path.getsize(nom_fichier)
    print(f"\nTaille du fichier binaire : {taille} octets")

    with open(nom_fichier, "rb") as f:
        donnees_binaires = f.read()
    bits = ''.join(f'{octet:08b}' for octet in donnees_binaires)
    print(f"\nChaîne des bits contenus dans le fichier :\n{bits}")

    points_decodes = parcours.lire_parcours(nom_fichier)
    deplacements_decodes = parcours.en_differentiel(points_decodes)

    print("\nListe des déplacements décodés :")
    print(deplacements_decodes)

    print("\nListe des points décodés :")
    print(points_decodes)

    sauvegarder_png("parcours.png", points)
    print('\nLe parcours graphique a été enregistré dans "parcours.png".')

racine = tk.Tk()
racine.title("Cliquez pour tracer le parcours (origine = centre, x droite, y haut)")
canevas = tk.Canvas(racine, width=TAILLE_CANEVAS, height=TAILLE_CANEVAS, bg="white")
canevas.pack()

points = []
canevas.bind("<Button-1>", enregistrer_clic)
racine.protocol("WM_DELETE_WINDOW", fermer)

racine.mainloop()


# Script Python : Générer les 64 minifloats (6 bits) au format (1, 3, 2)
# 1 bit de signe, 3 bits d'exposant, 2 bits de mantisse
# Hypothèse : biais = 3 (exposant de -3 à 4)

import math

for code in range(64):
    # Extraction du bit de signe (bit 5)
    signe = (code >> 5) & 0b1
    # Extraction des 3 bits d'exposant (bits 4 à 2)
    exposant = (code >> 2) & 0b111
    # Extraction des 2 bits de mantisse (bits 1 et 0)
    mantisse = code & 0b11

    biais = 3
    exposant_reel = exposant - biais

    if exposant == 0:
        # Sous-normaux : pas de 1 caché
        if mantisse == 0:
            valeur = 0.0
        else:
            # La plus petite puissance de 2 : 2**(1-biais) selon IEEE 754
            fraction = mantisse / 4.0
            valeur = ((-1) ** signe) * fraction * 2 ** (1 - biais)
    elif exposant == 0b111:
        # Cas spéciaux : Infini ou NaN (exposant au maximum)
        if mantisse == 0:
            valeur = math.inf if signe == 0 else -math.inf
        else:
            valeur = math.nan
    else:
        # Cas normalisé : 1 + mantisse/4 comme mantisse normalisée
        fraction = 1.0 + mantisse / 4.0
        valeur = ((-1) ** signe) * fraction * 2 ** exposant_reel

    print(f"{code:06b} : {valeur}")

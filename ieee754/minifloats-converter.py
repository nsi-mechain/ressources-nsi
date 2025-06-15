import tkinter as tk
import math

BIAS = 7

def flottant_vers_minifloat(val):
    if math.isnan(val):
        return "0 1111 001"
    if math.isinf(val):
        return f"{int(val < 0)} 1111 000"
    if val == 0:
        signe = 1 if math.copysign(1.0, val) < 0 else 0
        return f"{signe} 0000 000"

    signe = 0 if val > 0 else 1
    val = abs(val)
    exp = int(math.floor(math.log(val, 2)))
    e = exp + BIAS
    if not (0 < e < 15):
        return f"{signe} 1111 000" if e >= 15 else "0 0000 000"

    frac = val / (2 ** exp) - 1
    mantisse = int(round(frac * 8))
    if mantisse == 8:
        mantisse = 0
        e += 1
        if e >= 15:
            return f"{signe} 1111 000"

    bits = (signe << 7) | (e << 3) | mantisse
    binaire = f"{bits:08b}"
    return f"{binaire[0]} {binaire[1:5]} {binaire[5:]}"


def minifloat_vers_flottant(binaire):
    binaire = binaire.replace(" ", "")
    if len(binaire) != 8 or not all(c in '01' for c in binaire):
        return "Format binaire invalide"

    bits = int(binaire, 2)
    signe = (bits >> 7) & 0b1
    exposant = (bits >> 3) & 0b1111
    mantisse = bits & 0b111

    if exposant == 15:
        if mantisse == 0:
            return float('-inf') if signe else float('inf')
        else:
            return float('nan')
    if exposant == 0 and mantisse == 0:
        return -0.0 if signe else 0.0

    e = exposant - BIAS
    frac = 1 + mantisse / 8.0
    val = frac * (2 ** e)
    return -val if signe else val

def est_approximation(valeur, binaire):
    reconverti = minifloat_vers_flottant(binaire)
    try:
        if math.isnan(valeur) and math.isnan(reconverti):
            return False
        if math.isinf(valeur) and math.isinf(reconverti):
            return False
        if valeur == 0 and reconverti == 0:
            return math.copysign(1.0, valeur) != math.copysign(1.0, reconverti)
        return not math.isclose(valeur, reconverti, rel_tol=0.0, abs_tol=0.0)
    except Exception:
        return True

fenetre = tk.Tk()
fenetre.title("Encodeur/Décodeur MiniFloat (1,4,3)")

tk.Label(fenetre, text="Valeur flottante :").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entree_flottant = tk.Entry(fenetre, width=40)
entree_flottant.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

tk.Label(fenetre, text="Mini-float binaire :").grid(row=1, column=0, padx=10, pady=5, sticky='e')

# Les labels des champs binaire
tk.Label(fenetre, text="Sig").grid(row=1, column=1, padx=(0, 0))
tk.Label(fenetre, text="Exp").grid(row=1, column=2, padx=(0, 0))
tk.Label(fenetre, text="Mant").grid(row=1, column=3, padx=(0, 0))

# Champs rapprochés
entree_signe = tk.Entry(fenetre, width=2, justify="center")
entree_signe.grid(row=2, column=1, padx=(0, 0), pady=5)
entree_exposant = tk.Entry(fenetre, width=5, justify="center")
entree_exposant.grid(row=2, column=2, padx=(0, 0), pady=5)
entree_mantisse = tk.Entry(fenetre, width=3, justify="center")
entree_mantisse.grid(row=2, column=3, padx=(0, 0), pady=5)

label_etat = tk.Label(fenetre, text="", font=("Arial", 10, "italic"), anchor="w", justify="left")
label_etat.grid(row=5, column=0, columnspan=5, sticky="we", padx=10, pady=(5, 10))

def afficher_etat(msg, fg="black", bg="white"):
    label_etat.config(text=msg, fg=fg, bg=bg)

def encoder():
    try:
        val = float(entree_flottant.get())
        binval = flottant_vers_minifloat(val)
        signe, exposant, mantisse = binval.split()
        entree_signe.delete(0, tk.END)
        entree_exposant.delete(0, tk.END)
        entree_mantisse.delete(0, tk.END)
        entree_signe.insert(0, signe)
        entree_exposant.insert(0, exposant)
        entree_mantisse.insert(0, mantisse)
        reconverti = minifloat_vers_flottant(f"{signe}{exposant}{mantisse}")
        if est_approximation(val, f"{signe}{exposant}{mantisse}"):
            err_abs = abs(val - reconverti)
            err_rel = err_abs / abs(val) if val != 0 else float('inf')
            afficher_etat(f"Approximation ! Valeur proche = {reconverti} (Δabs={err_abs:.4f}, Δrel={err_rel:.2%})",
                          fg="#994d00", bg="#fff2cc")
        else:
            afficher_etat("Conversion exacte.", fg="darkgreen", bg="#e6ffcc")
    except Exception as e:
        afficher_etat(f"Erreur : {e}", fg="red", bg="#ffe6e6")

def decoder():
    try:
        signe = entree_signe.get().strip()
        exposant = entree_exposant.get().strip()
        mantisse = entree_mantisse.get().strip()
        binaire = f"{signe}{exposant}{mantisse}"
        val = minifloat_vers_flottant(binaire)
        if isinstance(val, str):
            afficher_etat(f"Erreur : {val}", fg="red", bg="#ffe6e6")
        else:
            entree_flottant.delete(0, tk.END)
            entree_flottant.insert(0, str(val))
            afficher_etat("Conversion réussie.", fg="darkgreen", bg="#e6ffcc")
    except Exception as e:
        afficher_etat(f"Erreur : {e}", fg="red", bg="#ffe6e6")

tk.Button(fenetre, text="Encoder → Binaire", command=encoder).grid(row=3, column=4, rowspan=2, padx=10, pady=5, sticky='e')
tk.Button(fenetre, text="Décoder → Flottant", command=decoder).grid(row=4, column=0, padx=10, pady=5, sticky='e')

# Remplissage d'exemple
signe, exposant, mantisse = flottant_vers_minifloat(1.0).split()
entree_flottant.insert(0, "1.0")
entree_signe.insert(0, signe)
entree_exposant.insert(0, exposant)
entree_mantisse.insert(0, mantisse)
afficher_etat("Exemple chargé : 1.0 → 0 0111 000", fg="darkgreen", bg="#e6ffcc")

fenetre.mainloop()

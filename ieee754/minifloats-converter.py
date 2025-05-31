import tkinter as tk
import math

BIAS = 7

def float_to_minifloat(val):
    if math.isnan(val):
        return "0 1111 001"
    if math.isinf(val):
        return f"{int(val < 0)} 1111 000"
    if val == 0:
        return "0 0000 000"

    sign = 0 if val > 0 else 1
    val = abs(val)
    exp = int(math.floor(math.log(val, 2)))
    e = exp + BIAS
    if not (0 < e < 15):
        return f"{sign} 1111 000" if e >= 15 else "0 0000 000"

    frac = val / (2 ** exp) - 1
    mantissa = int(round(frac * 8))
    if mantissa == 8:
        mantissa = 0
        e += 1
        if e >= 15:
            return f"{sign} 1111 000"

    bits = (sign << 7) | (e << 3) | mantissa
    binstr = f"{bits:08b}"
    return f"{binstr[0]} {binstr[1:5]} {binstr[5:]}"


def minifloat_to_float(binstr):
    binstr = binstr.replace(" ", "")
    if len(binstr) != 8 or not all(c in '01' for c in binstr):
        return "Format binaire invalide"

    bits = int(binstr, 2)
    sign = (bits >> 7) & 0b1
    exponent = (bits >> 3) & 0b1111
    mantissa = bits & 0b111

    if exponent == 15:
        if mantissa == 0:
            return float('-inf') if sign else float('inf')
        else:
            return float('nan')
    if exponent == 0 and mantissa == 0:
        return 0.0

    e = exponent - BIAS
    frac = 1 + mantissa / 8.0
    val = frac * (2 ** e)
    return -val if sign else val


def is_approximation(input_val, encoded_bits):
    if isinstance(encoded_bits, str) and " " in encoded_bits:
        reconverted = minifloat_to_float(encoded_bits)
        try:
            if math.isnan(input_val) and math.isnan(reconverted):
                return False
            if math.isinf(input_val) and math.isinf(reconverted):
                return False
            if input_val == 0 and reconverted == 0:
                return False
            relative_error = abs(input_val - reconverted) / abs(input_val)
            return relative_error > 0.01
        except Exception:
            return True
    return False


# Interface graphique
root = tk.Tk()
root.title("MiniFloat (1,4,3) Encodeur/Décodeur")

tk.Label(root, text="Valeur flottante :").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_float = tk.Entry(root, width=30)
entry_float.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Mini-float binaire :").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_bin = tk.Entry(root, width=30)
entry_bin.grid(row=1, column=1, padx=5, pady=5)

# Label d'état
label_error = tk.Label(root, text="", font=("Arial", 10, "italic"), anchor="w", justify="left")
label_error.grid(row=3, column=0, columnspan=2, sticky="we", padx=10, pady=(5, 10))


def set_status(msg, fg="black", bg="white"):
    label_error.config(text=msg, fg=fg, bg=bg)


def encode():
    try:
        val = float(entry_float.get())
        binval = float_to_minifloat(val)
        entry_bin.delete(0, tk.END)
        entry_bin.insert(0, binval)
        if is_approximation(val, binval):
            set_status("Attention : valeur approximative.", fg="#994d00", bg="#fff2cc")
        else:
            set_status("Aucune erreur.", fg="darkgreen", bg="#e6ffcc")
    except Exception as e:
        set_status(f"Erreur : {e}", fg="red", bg="#ffe6e6")


def decode():
    try:
        binstr = entry_bin.get().strip()
        val = minifloat_to_float(binstr)
        if isinstance(val, str):  # erreur texte retournée
            set_status(f"Erreur : {val}", fg="red", bg="#ffe6e6")
        else:
            entry_float.delete(0, tk.END)
            entry_float.insert(0, str(val))
            set_status("Aucune erreur.", fg="darkgreen", bg="#e6ffcc")
    except Exception as e:
        set_status(f"Erreur : {e}", fg="red", bg="#ffe6e6")


# Boutons
tk.Button(root, text="Encoder → Binaire", command=encode).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Décoder → Float", command=decode).grid(row=2, column=1, padx=5, pady=10)

# Pré-remplissage initial
entry_float.insert(0, "1.0")
entry_bin.insert(0, float_to_minifloat(1.0))
set_status("Exemple chargé : 1.0 → 0 0111 000", fg="darkgreen", bg="#e6ffcc")

root.mainloop()

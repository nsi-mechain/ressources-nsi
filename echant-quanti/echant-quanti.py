import numpy as np
import matplotlib.pyplot as plt

n_bits = 4
nb_echant = 20

# Définition du signal analogique (y entre 0 et  1 pour x variant de 0 à 1)
def f(t):
    return 0.25 + 0.35 * (np.sin(8*t) + np.sin(4*t))
    
# Générer des données pour la sinusoïde
x = np.arange(0, 1, 0.01); print(x)
y = f(x) * (2**n_bits-1); print(y)
# Créer le graphe
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", linewidth=3)

# Générer des données pour la sinusoïde quantifiée
x = np.arange(0, 1, 1/nb_echant); print(x)
y = np.round(f(x) * (2**n_bits-1)); print(y)
# Créer le graphe
ax.plot(x, y, 'o', color="red")

# Définir les positions des graduations sur l'axe des y
y_ticks = np.arange(0, 2 ** n_bits, 1)
ax.set_yticks(y_ticks)
plt.yticks(fontsize=10)
# Ajouter une grille horizontale
ax.yaxis.set_major_formatter(lambda x, code_binaire: f"{int(x):0{n_bits}b}")
ax.grid(axis='y', linestyle='-', color="red", alpha=0.25)

# Définir les positions des graduations sur l'axe des x
x_ticks = np.arange(0, 1, 1/nb_echant)
ax.set_xticks(x_ticks)
plt.xticks(fontsize=10, rotation='vertical')
# Ajouter une grille verticale
ax.grid(axis='x', linestyle='--')

# Afficher le graphe
plt.show()

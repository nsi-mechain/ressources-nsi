# Fiche explicative des scripts `gene_wav.py` et `extrait_wav.py`

Cette fiche explique le fonctionnement de deux scripts Python utilisés pour générer puis analyser un fichier audio stéréo au format WAV. Les deux scripts sont complémentaires : le premier crée un fichier contenant deux signaux sinusoïdaux (un par canal), le second extrait les premiers échantillons de ce fichier et les affiche graphiquement.

---

## 1. `gene_wav.py` — Génération d’un fichier stéréo WAV

Ce script permet de générer un fichier audio `stereo_sinus.wav` contenant deux sinusoïdes de fréquences différentes sur les voies gauche et droite.

```python
import wave
import struct
import math

# Paramètres
samplerate = 44100  # Hz
duration = 0.1        # seconde
amplitude = 0.5     # amplitude "relative" (1.0 = max)
freq_left = 1000    # Hz (voie gauche)
freq_right = 10000  # Hz (voie droite)
filename = "stereo_sinus.wav"

max_amp = int(amplitude * 32767)  # amplitude max pour 16 bits

with wave.open(filename, "w") as wav:
    wav.setnchannels(2)         # stéréo
    wav.setsampwidth(2)         # 16 bits
    wav.setframerate(samplerate)

    for n in range(int(samplerate * duration)):
        # Calcul des deux sinus
        left = int(max_amp * math.sin(2 * math.pi * freq_left * n / samplerate))
        right = int(max_amp * math.sin(2 * math.pi * freq_right * n / samplerate))
        # Encodage en little-endian
        frame = struct.pack('<hh', left, right)
        wav.writeframesraw(frame)

print("Fichier créé :", filename)
```

### Explications principales

- **Bibliothèques utilisées** :
  - `wave` : pour la gestion du format WAV (lecture/écriture de fichiers audio PCM).
  - `struct` : pour le codage des entiers (échantillons) en binaire.
  - `math` : pour le calcul des valeurs sinusoïdales.
- **Paramètres modifiables** :
  - `samplerate` : taux d’échantillonnage (nombre d’échantillons par seconde)
  - `duration` : durée totale du signal généré
  - `amplitude` : amplitude maximale des sinusoïdes (0.0 à 1.0)
  - `freq_left` / `freq_right` : fréquences des voies gauche/droite
- **Boucle principale** :
  - Pour chaque échantillon, calcule la valeur de chaque sinus (gauche et droite)
  - Les deux valeurs (gauche/droite) sont encodées dans un bloc de 4 octets (2 x 16 bits)
  - Les données sont écrites successivement dans le fichier WAV

---

## 2. `extrait_wav.py` — Extraction et affichage d’échantillons

Ce script extrait les 50 premiers échantillons du fichier WAV stéréo généré, puis affiche l’évolution de l’amplitude pour chaque canal (gauche/droite) à l’aide de matplotlib.

```python
import wave
import struct
import matplotlib.pyplot as plt

# Chemin vers le fichier WAV
filename = "stereo_sinus.wav"

nb_samples = 50

with wave.open(filename, "rb") as wav:
    nchannels = wav.getnchannels()
    sampwidth = wav.getsampwidth()
    framerate = wav.getframerate()
    nframes = wav.getnframes()

    # Positionnement et lecture
    wav.setpos(0)
    frames = wav.readframes(nb_samples)

    # Extraction des deux voies
    gauche = []
    droite = []
    for i in range(nb_samples):
        frame = frames[i*4:(i+1)*4]  # 4 octets par frame (2 x 16 bits)
        g, d = struct.unpack("<hh", frame)
        gauche.append(g)
        droite.append(d)

# Tracé avec matplotlib
plt.figure(figsize=(8, 4))
plt.plot(range(1, nb_samples+1), gauche, marker='o', label='Gauche')
plt.plot(range(1, nb_samples+1), droite, marker='x', label='Droite')
plt.title('50 échantillons à partir du début (stéréo)')
plt.xlabel('N° d\'échantillon')
plt.ylabel('Amplitude (16 bits)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

### Explications principales

- **Lecture du fichier WAV** : extraction des paramètres (nombre de canaux, largeur d’échantillon, etc.)
- **Lecture des échantillons** :
  - On lit les 50 premiers échantillons (chaque échantillon stéréo = 4 octets)
  - Pour chaque frame, on sépare les deux canaux (gauche et droite)
  - Les valeurs sont stockées dans deux listes
- **Affichage graphique** :
  - Tracé de chaque voie sur le même graphe
  - Visualisation directe de la forme des deux sinusoïdes

---

## Utilisation typique

1. Exécuter d’abord `gene_wav.py` pour générer le fichier stéréo contenant les deux sinusoïdes.
2. Exécuter ensuite `extrait_wav.py` pour extraire et visualiser les premiers échantillons du fichier généré.

Cela permet d’illustrer concrètement la structure d’un fichier audio stéréo, ainsi que la représentation numérique des signaux audio.


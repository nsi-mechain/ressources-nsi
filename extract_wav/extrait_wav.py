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

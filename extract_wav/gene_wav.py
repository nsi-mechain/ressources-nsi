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

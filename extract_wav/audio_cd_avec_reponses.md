## 🎵 Illustration du débit audio CD avec une bande de papier

Voici l'idée : vous avez une bande de papier quadrillé de 32 mm de largeur où chaque bit est représenté par un carré de 1 mm de côté. Les 32 bits nécessaires pour un échantillon stéréo (16 bits par canal) sont donc matérialisés sur chaque ligne de la bande.

Le flux audio d’un CD est de `2x16 bits / 44,1 kHz`, ce qui détermine la vitesse à laquelle la bande doit défiler.

### 📝 Questionnaire avec réponses

**1. Combien de bits sont nécessaires pour représenter un seul échantillon stéréo ?**
> 32 bits (16 bits pour chaque canal), soit 4 octets.

**2. Calculez le débit binaire (bits par seconde) d’un CD audio.**
> 44 100 échantillons/s × 32 bits = 1 411 200 bits/s = **1,4112 Mb/s**

**3. À quelle vitesse (en mètres par seconde) la bande doit-elle défiler pour illustrer le flux d’un CD audio en temps réel ?**
> **44 100 échantillons/s × 1 mm = 44 100 mm/s = **44,1 m/s**.

**4. À quelle vitesse en kilomètres par heure cela correspond-il ?**
> 44,1 m/s × 3,6 ≈ **159 km/h**.

**6. Quelle sera la longueur totale de la bande nécessaire pour représenter un CD entier de durée 74 minutes ?**
> 44,1 m/s × 4 440 s = 196 284 mètres ≈ **196 km**.

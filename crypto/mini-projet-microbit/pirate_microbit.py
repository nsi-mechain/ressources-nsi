from microbit import *
import radio

# 1. Activation de la radio
radio.on()

# 2. Configuration sur le canal (groupe) 50
radio.config(group=50)

display.show(Image.HAPPY)
sleep(1000)
display.clear()

while True:
    # 3. Tentative de lecture d'un message entrant
    message = radio.receive()
    
    # 4. Si un message est reçu (n'est pas None)
    if message:
        # On affiche le texte reçu sur la matrice LED
        display.scroll(message)
    
    sleep(100)

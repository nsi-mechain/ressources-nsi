# Projet RSA microbit - POV of "Paul"

from microbit import *
import radio

radio.config(group=50)
radio.on()

message_initial = 76

display.scroll("READY")
display.show(Image.HAPPY)
sleep(1000)
display.clear()

def pow_mod(base, exposant, modulo):
    resultat = 1
    base = base % modulo
    
    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * base) % modulo
        exposant = exposant // 2
        base = (base * base) % modulo
        
    return resultat



while True:
    message = radio.receive()
    if message:
        
        if ";" in message:   #verification que c’est une clef
            try:
                e_str, n_str = message.split(";")
                e = int(e_str.strip())
                n = int(n_str.strip())
                
                display.scroll("KEY OK")
                display.show(Image.YES)
                sleep(1000)
                display.clear()
                
                message_chiffre = pow_mod(message_initial, e, n)
                radio.send(str(message_chiffre))
                
                display.scroll("SENT")
                display.show(Image.YES)
                sleep(1000)
                display.clear()
                
            except:
                display.show(Image.NO)
                sleep(1000)
                display.clear()
                display.show(Image.NO)
                sleep(1000)
                display.scroll("FORMAT ERROR")
               
                

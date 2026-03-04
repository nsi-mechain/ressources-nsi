from microbit import *
import radio

def power_mod(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

radio.config(group=50)
radio.on()

p = 17
q = 23

n = p * q
phi = (p - 1) * (q - 1)

e = 3
while phi % e == 0:
    e += 2

d = 1
while (e * d) % phi != 1:
    d += 1

display.scroll("CLE")

while True:
    
    # Envoi de e;n
    if button_a.was_pressed():
        radio.send("{};{}".format(e, n))
        display.scroll("ENVOYE")
    
    # Réception du message chiffré
    message = radio.receive()
    if message:
        c = int(message)
        m = power_mod(c, d, n)
        display.scroll("M={}".format(m))

from turtle import *


def Koch(n, d):
    if n == 0:
        forward(d)
    else:
        Koch(n-1, d/3)
        left(60)
        Koch(n-1, d/3)
        right(120)
        Koch(n-1, d/3)
        left(60)
        Koch(n-1, d/3)


def flocon(n, d):
    for k in range(3):
        Koch(n, d)
        right(120)


flocon(2, 400)
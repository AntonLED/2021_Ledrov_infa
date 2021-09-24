import math
import turtle as tl

i = 1
while True:
    phi = i / 10 * math.pi
    dx = phi * math.cos(phi)
    dy = phi * math.sin(phi)
    tl.goto(dx, dy)
    i += 1

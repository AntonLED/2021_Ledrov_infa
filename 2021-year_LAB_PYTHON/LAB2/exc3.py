import turtle as tl

tl.speed(0)

tl.shape('circle')
tl.shapesize(0.2)

x = 0
y = 0

Vx = 5
Vy = 50

g = 9.81

dt = 0.05

y_lim = tl.pos()[1]

while True:
    tl.goto(x, y)
    x += Vx * dt
    y += Vy * dt - g * dt ** 2 / 2
    Vy += -g * dt
    if y < y_lim - Vy * dt:
        Vy = -0.75 * Vy

import math
import turtle as tl

tl.speed(0)


def circle(R):
    N = int(2 * math.pi * R / 2)

    for _ in range(N):
        tl.forward(2)
        tl.right(360 / N)


tl.penup()
tl.goto(50, 0)
tl.pendown()
tl.right(90)
circle(50)

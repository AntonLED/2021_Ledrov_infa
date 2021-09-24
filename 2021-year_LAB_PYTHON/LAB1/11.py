import math
import turtle as tl

tl.speed(0)


def circle(R):
    N = int(2 * math.pi * R / 2)

    for _ in range(N):
        tl.forward(2)
        tl.right(180 / N)


tl.right(90 * 3)
while True:
    circle(20)
    circle(5)

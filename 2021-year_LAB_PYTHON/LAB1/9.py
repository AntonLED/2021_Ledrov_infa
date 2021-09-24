import math
import turtle as tl

tl.speed(0)


def circle(R, param=False):
    N = int(2 * math.pi * R / 3)

    if param:
        for _ in range(N):
            tl.forward(3)
            tl.left(360 / N)
    else:
        for _ in range(N):
            tl.forward(3)
            tl.right(360 / N)


for _ in range(3):
    circle(30)
    circle(30, True)
    tl.right(60)

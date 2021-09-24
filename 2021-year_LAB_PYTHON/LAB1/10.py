import math
import turtle as tl

tl.speed(0)


def circle(R, param=False):
    N = int(2 * math.pi * R / 2)

    if param:
        for _ in range(N):
            tl.forward(2)
            tl.left(360 / N)
    else:
        for _ in range(N):
            tl.forward(2)
            tl.right(360 / N)


tl.right(90)
for i in range(1, 16):
    circle(10 + i * 2, bool(i % 2))

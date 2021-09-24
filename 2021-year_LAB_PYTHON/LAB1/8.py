import math
import turtle as tl

tl.speed(0)

da = 0


def reg_gon(a, n):
    tl.left(90 - 180 / n)
    for _ in range(n):
        tl.left(360 / n)
        tl.forward(a)
    tl.right(90 - 180 / n)

    R = a / 2 / math.sin(math.radians(180 / n))

    tl.penup()
    tl.forward(20)
    tl.pendown()

    return 2 * (R + 20) * math.sin(math.radians(180 / (n + 1))) - a


for i in range(3, 14):
    da += reg_gon(40 + da, i)

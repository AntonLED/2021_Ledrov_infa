import math
import turtle as tl

tl.speed(0)


def half_circle(R):
    N = int(2 * math.pi * R / 2)

    for _ in range(N):
        tl.forward(2)
        tl.right(180 / N)


def circle(R):
    N = int(2 * math.pi * R / 2)

    for _ in range(N):
        tl.forward(2)
        tl.right(360 / N)


def draw_smile():
    tl.penup()
    tl.backward(70)
    tl.right(270)
    tl.pendown()

    tl.begin_fill()
    circle(70)
    tl.color('yellow')
    tl.end_fill()

    tl.color('black')
    tl.penup()
    tl.goto(tl.pos()[0] + 35, tl.pos()[1] + 35)
    tl.pendown()

    tl.begin_fill()
    circle(10)
    tl.color('blue')
    tl.end_fill()

    tl.penup()
    tl.goto(tl.pos()[0] + 50, tl.pos()[1] + 0)
    tl.pendown()

    tl.begin_fill()
    circle(10)
    tl.end_fill()

    tl.penup()
    tl.goto(0, tl.pos()[1] - 20)
    tl.pendown()

    tl.width(3)
    tl.right(180)
    tl.color('black')
    tl.forward(20)

    tl.penup()
    tl.goto(0, 0)
    tl.left(90)
    tl.forward(38)
    tl.pendown()

    tl.color("red")
    tl.width(3)
    tl.right(90)
    half_circle(20)


draw_smile()

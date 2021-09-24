import turtle as tl

tl.speed(0)

tl.penup()
tl.goto(-25, 25)
tl.pendown()

for i in range(1, 11):
    tl.forward(10 * i)
    tl.right(90)
    tl.forward(10 * i)
    tl.right(90)
    tl.forward(10 * i)
    tl.right(90)
    tl.forward(10 * i)
    tl.right(90)
    tl.penup()
    tl.goto(tl.pos()[0] - 5, tl.pos()[1] + 5)
    tl.pendown()

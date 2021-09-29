import turtle as tl
from random import randint

tl.speed(0)
number_of_turtles = 50
steps_of_time_number = 100000000000

dt = 1
x_lim = 300
y_lim = 300

tl.penup()
tl.shape('circle')
tl.shapesize(0.01)
tl.left(90)
tl.goto(-1 * x_lim, -1 * y_lim)
tl.pendown()
tl.forward(2 * x_lim)
tl.right(90)
tl.forward(2 * x_lim)
tl.right(90)
tl.forward(2 * x_lim)
tl.right(90)
tl.forward(2 * x_lim)
tl.right(90)

tl.tracer(50)

positions = []
vels = []

pool = [tl.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.speed(0)
    unit.penup()
    unit.shapesize(0.5)
    unit.speed(0)
    x = randint(-1 * x_lim, x_lim) * 1.
    y = randint(-1 * y_lim, y_lim) * 1.
    unit.goto(0.9 * x, 0.9 * y)
    positions.append([0.9 * x, 0.9 * y])
    vels.append([(-1) ** randint(5, 6) * 1.5, (-1) ** randint(5, 6) * 1.5])
    unit.right(randint(0, 361))

for i in range(steps_of_time_number):
    for unit in pool:
        positions[pool.index(unit)][0] = positions[pool.index(unit)][0] + vels[pool.index(unit)][0] * dt
        positions[pool.index(unit)][1] = positions[pool.index(unit)][1] + vels[pool.index(unit)][1] * dt
        if abs(positions[pool.index(unit)][0]) > x_lim - 5:
            vels[pool.index(unit)][0] = -1 * vels[pool.index(unit)][0]
        if abs(positions[pool.index(unit)][1]) > y_lim - 5:
            vels[pool.index(unit)][1] = -1 * vels[pool.index(unit)][1]
        unit.goto(positions[pool.index(unit)][0], positions[pool.index(unit)][1])

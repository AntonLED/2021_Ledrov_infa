import turtle as tl

tl.speed(0)

tl.shape('circle')
tl.shapesize(0.001)

moves_sticks = [[0, 0, 1, 0, 1], [1, 0, 1, 1, 2], [1, 1, 1, 2, 3],
                [1, 2, 0, 2, 4], [0, 2, 0, 1, 5], [0, 1, 0, 0, 6],
                [1, 0, 0, 1, 7], [0, 1, 1, 1, 8], [1, 1, 0, 2, 9]]

num_font = 0
sticks_to_num = []

with open('exc2.txt') as file:
    for line in file:
        if "font: " in line:
            num_font = int(line[6::])
        elif "numbers:\n" in line:
            continue
        else:
            sticks_to_num.append(tuple(map(int, line.split(", "))))

h = num_font
w = num_font

for m in moves_sticks:
    m[0] = m[0] * h
    m[2] = m[2] * h
    m[1] = -1 * m[1] * w
    m[3] = -1 * m[3] * w


def tl_num():
    x = 0
    for k in list(map(int, ' '.join(input()).split())):
        for j in sticks_to_num[k]:
            for i in moves_sticks:
                if j == i[4]:
                    tl.penup()
                    tl.goto(x + i[0], i[1])
                    tl.pendown()
                    tl.goto(x + i[2], i[3])
                    tl.penup()
        x += num_font + 5


tl_num()
tl.exitonclick()

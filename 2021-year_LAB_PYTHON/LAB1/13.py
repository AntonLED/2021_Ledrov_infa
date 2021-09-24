import turtle as tl

tl.speed(0)


def reg_gon(a, n, pos=False):
    positions = []
    tl.left(90 - 180 / n)
    for _ in range(n):
        tl.left(360 / n)
        tl.forward(a)
        if pos:
            positions.append((tl.pos()[0], tl.pos()[1]))
    tl.right(90 - 180 / n)
    if pos:
        return positions


def star(n, a):
    tl.penup()
    dots_pos = reg_gon(a, n, True)
    tl.pendown()
    i = 0
    c = 0
    while True:
        i += int((n - 1) / 2)
        tl.goto(dots_pos[i % n][0], dots_pos[i % n][1])
        c += 1
        if c == n + 1:
            break


star(9, 50)

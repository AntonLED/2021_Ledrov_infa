import turtle as tl

n = int(input("Введите количество лап: "))

for i in range(n):
    tl.forward(100)
    tl.stamp()
    tl.backward(100)
    tl.right(360 / n)

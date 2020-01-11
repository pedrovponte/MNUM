import math
import matplotlib.pyplot as plt

def f(x,y):
    return math.sin(x)

def rk4(x,y,h):
    tuplo = ()
    listax = []
    listay = []
    for i in range(500):
        x_anterior = x
        x = x_anterior + h
        delta_1 = h * f(x_anterior, y)
        delta_2 = h * f(x_anterior + h / 2, y + delta_1 / 2)
        delta_3 = h * f(x_anterior + h / 2, y + delta_2 / 2)
        delta_4 = h * f(x_anterior + h, y + delta_3)
        
        y = y + delta_1 / 6 + delta_2 / 3 + delta_3 / 3 + delta_4 / 6
        
        tuplo = (x,y)
        listax.append(tuplo[0])
        listay.append(tuplo[1])
    plt.plot(listax, listay)
    plt.show()
    print("x: ", x)
    return y

h = 0.1

r1 = rk4(0, 0, h)
print("y1: ", r1)
r2 = rk4(0, 0, h / 2)
print("y2: ", r2)
r3 = rk4(0, 0, h / 4)
print("y3: ", r3)
r4 = rk4(0, 0, h / 8)
print("y4: ", r4)

quociente = (r2 - r1) / (r3 - r2)
print("quociente: ", quociente)
erro = (r3 - r2) / 15
print("erro: ", erro)
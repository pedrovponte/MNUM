import math
import matplotlib.pyplot as plt

def f(x,y):
    return math.sin(x)

#tuplo = ()
#listax = []
#listay = []

def Euler(x,y,h):
    tuplo = ()
    listax = []
    listay = []
    for i in range(1000):         
        x_anterior = x
        x = x_anterior + h
        y = y + h * f(x_anterior, y)
        tuplo = (x,y)
        listax.append(tuplo[0])
        listay.append(tuplo[1])
    plt.plot(listax, listay)
    plt.show()
    print("x:", x)
    return y


h = 0.1

r1 = Euler(0, 0, 0.5)
print("y1:", r1)
r2 = Euler(0, 0, 0.5/2)
print("y2:", r2)
r3 = Euler(0, 0, 0.5/4)
print("y3:", r3)
r4 = Euler(0, 0, 0.5/8)
print("y4:", r4)

quociente = (r2 - r1) / (r3 - r2)
erro = (r3 - r2)
print("quociente", quociente) 
print("erro:", erro)
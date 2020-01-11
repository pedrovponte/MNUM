import math

def f(x):
    return math.sin(x)

def simpson(a,b,n):
    total = 0
    h = (b - a) / n
    for i in range(1, n, 2):
        total += 4 * f(a + i * h)
    for i in range(2, n, 2):
        total += 2 * f(a + i * h)
    total += f(a) + f(a + n * h)
    total *= h / 3
    return total

r1 = simpson(math.pi/2, math.pi, 4)
r2 = simpson(math.pi/2, math.pi, 8)
r3 = simpson(math.pi/2, math.pi, 16)

coeficiente = (r2 - r1) / (r3 - r2)

print("r1: ", r1)
print("r2: ", r2)
print("r3: ", r3)
print("coeficiente: ", coeficiente)

erro = (r3 - r2) / 15
print("erro: ", erro)
 
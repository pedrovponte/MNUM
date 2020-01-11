import math

def f(x):
    return math.sin(x)

def trapezio(a,b,n):
    h = (b - a) / n
    total = 0
    for i in range(1,n):
        total += 2 * f(a + i * h)
    total += f(a) + f(a + n * h)
    total *= h / 2
    return total

r1 = trapezio(0, 2, 4)
r2 = trapezio(0, 2, 8)
r3 = trapezio(0, 2, 16)

coeficiente = (r2 - r1) / (r3 - r2)

print("r1: ", r1)
print("r2: ", r2)
print("r3: ", r3)
print("coeficiente: ", coeficiente)

erro = (r3 - r2) / 3
print("erro: ", erro)
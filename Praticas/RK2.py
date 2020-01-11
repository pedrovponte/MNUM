def f(x,y):
    return x*x + y*y

def rk2(x,y,b,h):
    while(x < b - 0.01):
        x_anterior = x
        x = x_anterior + h
        y = y + h * f(x_anterior + h/2, y + h/2 * f(x_anterior,y))
    print(x,y)
    return y


h = 0.1
b = 1.4

r1 = rk2(0, 0, b, h)
r2 = rk2(0, 0, b, h/2)
r3 = rk2(0, 0, b, h/4)

quociente = (r2 - r1) / (r3 - r2)
print("quociente: ", quociente)
erro = (r3 - r2) / 3
print("erro: ", erro)

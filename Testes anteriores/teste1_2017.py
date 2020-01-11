import math

def f(x):
    return (x - 3.6) + (math.cos(x + 1.2))**3

def derivate(x):
    return 1 - 3 * (math.cos(x + 1.2))**2 * math.sin(x + 1.2)

def newton(guess):
    last = 0
    x = guess
    while(abs(x-last) > 10e-5):
        last = x
        x = x - f(x) / derivate(x)
        print(x)
    return x

print(newton(0.5))
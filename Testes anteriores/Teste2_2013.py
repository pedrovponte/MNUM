import math

def f(t, x):
    return math.sin(2*x) + math.sin(2 * t)

def RK4(h, t, x):
    print("t: ", t)
    print("x: ", x)
    for i in range(4):
        t_anterior = t
        t = t_anterior + h
        delta_1 = h * f(t_anterior, x)
        delta_2 = h * f(t_anterior + h/2, x + delta_1/2)
        delta_3 = h * f(t_anterior + h / 2, x + delta_2 / 2)
        delta_4 = h * f(t_anterior + h, x + delta_3)
        x = x + delta_1 / 6 + delta_2 / 3 + delta_3 / 3 + delta_4 / 6
        print("t: ", t)
        print("x: ", x)
    
s1 = RK4(0.125, 1, 1)
    
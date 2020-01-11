import math

#ex 1 - metodo de euler

#def f(t,y):
#    return y/(t-1)
#
#def euler(t,y,h):
#    print("t: ", t, "y: ", y)
#    for i in range(2):
#        t_anterior = t
#        t += h
#        y = y + h * f(t_anterior,y)
#        print("t: ", t, "y: ", y)
#
#euler(2,2,0.25)

#ex 1 - rk4

#def rk4(t,y,h):
#    for i in range(3):
#        t_anterior = t
#        t += h
#        delta1 = h * f(t_anterior, y)
#        delta2 = h * f(t_anterior + h/2, y + delta1/2)
#        delta3 = h * f(t_anterior + h/2, y + delta2/2)
#        delta4 = h * f(t_anterior + h, y + delta3)
#        
#        y = delta1/6 + delta2/3 + delta3/3 + delta4/6
#        print("t: ", t, "y: ", t, "delta1: ", delta1, "delta2: ", delta2, "delta3: ", delta3, "delta4: ", delta4)
#
#rk4(2,2,0.25)

#ex 3 - metodo do gradiente

#def f(x,y):
#    return -1.7*x*y + 12*y + 7*x*x - 8*x
#
#def fx(x,y):
#    return -1.7*y + 14*x - 8
#
#def fy(x,y):
#    return -1.7*x + 12
#
#def gradiente(x,y,h):
#    xn = x - h * fx(x,y)
#    yn = y - h * fy(x,y)
#    
#    if (f(xn,yn) < f(x,y)):
#        h *= 2
#        x = xn
#        y = yn
#    
#    if (f(xn,yn) > f(x,y)):
#        h /= 2
#    
#    print(f(x,y))
#    
#gradiente(2.4,4.3,0.1)

#ex 5 - metodo de newton

#def f1(x,y):
#    return x*x - y - 2
#
#def f2(x,y):
#    return -x + y*y - 2
#
#def f1x(x,y):
#    return 2*x
#
#def f2x(x,y):
#    return -1
#
#def f1y(x,y):
#    return -1
#
#def f2y(x,y):
#    return 2*y
#
#def jacobian(x,y):
#    return f1x(x,y) * f2y(x,y) - f1y(x,y) * f2x(x,y) 
#
#def newton(x,y):
#    for i in range(2):
#        x = x - (f1(x,y) * f2y(x,y) - f1y(x,y) * f2(x,y)) / jacobian(x,y)
#        y = y - (f1x(x,y) * f2(x,y) - f1(x,y) * f2x(x,y)) / jacobian(x,y)
#        print("x: ",x,"y: ", y)
#
#newton(1.5,0.8)

#ex 7 - metodo de simpson

def f(x):
    return math.pow(math.e,1.5*x)

def simpson(a,b,h,n):
    total = 0
    for i in range(1,n,2):
        total += 4 * f(a + i * h)
    for i in range(2,n,2):
        total += 2 * f(a + i * h)
    total += f(a) + f(a + n * h)
    total *= h/3
    return total

r1 = simpson(2.5,3,0.125,2)
print(r1)
r2 = simpson(2.5,3,0.125/2,4)
print(r2)
r3 = simpson(2.5,3,0.125/4,8)
print(r3)

qc = (r2 - r1) / (r3 - r2)
print(qc)

erro = (r3 - r2) / 15
print(erro)
    
import math

#ex 1 - RK4

#def f(t,y,z):
#    return z
#
#def g(t,y,z):
#    return 0.5 + t**2 + t*z
#
#def rk4(t,y,z,h):
#    print("0: ", t, y)
#    for i in range(1,3):
#        t_anterior = t
#        t += h
#        delta1_y = h * f(t_anterior,y,z)
#        delta1_z = h * g(t_anterior,y,z)
#        delta2_y = h * f(t_anterior + h/2, y + delta1_y/2, z + delta1_z/2)
#        delta2_z = h * g(t_anterior + h/2, y + delta1_y/2, z + delta1_z/2)
#        delta3_y = h * f(t_anterior + h/2, y + delta2_y/2, z + delta2_z/2)
#        delta3_z = h * g(t_anterior + h/2, y + delta2_y/2, z + delta2_z/2)
#        delta4_y = h * f(t_anterior + h, y + delta3_y, z + delta3_z)
#        delta4_z = h * g(t_anterior + h, y + delta3_y, z + delta3_z)
#        
#        y = y + delta1_y/6 + delta2_y/3 + delta3_y/3 + delta4_y/6
#        z = z + delta1_z/6 + delta2_z/3 + delta3_z/3 + delta4_z/6
#        
#        print(i, ": ", t, y)
#        
#rk4(0,0,1,0.25)

#ex 3 - gradiente

#def f(x,y):
#    return 3*x**2 - x*y + 11*y + y**2 - 8*x
#
#def fx(x,y):
#    return 6*x - y -8
#
#def fy(x,y):
#    return -x + 11 + 2*y
#
#def gradiente(x,y,h):
#    xn = 0
#    yn = 0
#    gradient_x = fx(x,y)
#    gradient_y = fy(x,y)
#    print("Iteraçao 0: ",x,y,f(x,y),gradient_x, gradient_y)
#    xn = x - h * fx(x,y)
#    yn = y - h * fy(x,y)
#    if(f(xn,yn) < f(x,y)):
#        h *= 2
#        x = xn
#        y = yn
#        print("Iteração 1: ",x,y,f(x,y),gradient_x,gradient_y)
#    else:
#        h /= 2
#    
#gradiente(2,2,0.5)

#ex 4 - metodo simpson

#def f(x):
#    return math.exp(1.5*x)
#
#def simpson(a,b,h):
#    total = 0
#    n = int((b - a) / h)
#    for i in range(1,n,2):
#        total += 4 * f(a + i * h)
#    for i in range(2,n,2):
#        total += 2 * f(a + i * h)
#    total += f(a) + f(a + n * h)
#    total *= h/3
#    return total
#
#r1 = simpson(1,1.5,0.125)
#print("r1: ",r1)
#r2 = simpson(1,1.5,0.125/2)
#print("r2: ",r2)
#r3 = simpson(1,1.5,0.125/4)
#print("r3: ",r3)
#
#qc = (r2 - r1) / (r3 - r2)
#print("qc: ",qc)
#
#erro = (r3 - r2) / 15
#print("erro: ", erro)

#ex 5 - metodo de newton

def f(x):
    return (x-3.7) + math.pow(math.cos(x+1.2),3)

def fx(x):
    return 1 - 3*math.pow(math.cos(x+1.2),2)*math.sin(x+1.2)

def newton(guess):
    x = guess
    x = x - f(x)/fx(x)
    return x

r1 = newton(3.8)
print(r1)
    
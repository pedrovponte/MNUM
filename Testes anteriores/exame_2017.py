import math

#ex.1 - regra aurea

#def f(x):
#    return (x-4)**2 + x**4
#
#def aurea(x1,x2):
#    b = (math.sqrt(5)-1)/2
#    a = b*b
#    result = 0
#    while(x2-x1 > 0.001):
#        x3 = x1 + a*(x2-x1)
#        x4 = x1 + b*(x2-x1)
#        
#        if(f(x3) < f(x4)):
#            x2 = x4
#            x1 = x1
#        else:
#            x1 = x3
#            x2 = x2
#        result = (x1+x2)/2
#        
#    return result
#
#print(aurea(1,3))

#ex.2 - simpson e trapezios

#def f(x):
#    return math.sqrt(1+(2.5*math.exp(2.5*x))**2)
#
#def simpson(a,b,h):
#    total = 0
#    n = int((b-a)/h)
#    for i in range(1,n,2):
#        total += 4 * f(a + i * h)
#    for i in range(2,n,2):
#        total += 2 * f(a + i * h)
#    total += f(a) + f(a + n * h)
#    total *= h / 3
#    return total
#
#def trapezios(a,b,h):
#    total = 0
#    n = int((b - a)/h)
#    for i in range(1,n):
#        total += 2 * f(a + i * h)
#    total += f(a) + f(a + n * h)
#    total *= h / 2
#    return total
#
#r1 = simpson(0,1,0.125)
#r2 = simpson(0,1,0.125/2)
#r3 = simpson(0,1,0.125/4)
#qc = (r2 - r1) / (r3 - r2)
#er = (r3 - r2) / 15
#r1t = trapezios(0,1,0.125)
#r2t = trapezios(0,1,0.125/2)
#r3t = trapezios(0,1,0.125/4)
#qct = (r2t - r1t) / (r3t - r2t) 
#ert = (r3t - r2t) / 3
#print("SIMPSON:")
#print("r1: ", r1)
#print("r2: ", r2)
#print("r3: ", r3)
#print("qc: ", qc)
#print("erro: ", er)
#print("TRAPEZIOS:")
#print("r1: ", r1t)
#print("r2: ", r2t)
#print("r3: ", r3t)
#print("qc: ", qct)
#print("erro: ", ert)

#ex3 - metodos de newton e picard-peano

#def f(x):
#    return math.exp(x) - x - 5
#
#def df(x):
#    return math.exp(x) - 1
#
#def g(x):
#    return math.log(x + 5)
#
#def newton(x):
#    x_anterior = 100
#    i = 0
#    while(abs(x - x_anterior) > 0.00001):
#        x_anterior = x
#        x = x - f(x)/df(x)
#        i += 1
#    print("NEWTON")
#    print("Iteration ", i, ": ", x)
#
#def picard_p(x):
#    x_anterior = 100
#    i = 0
#    while(abs(x - x_anterior) > 0.00001):
#        x_anterior = x
#        x = g(x)
#        i += 1
#    print("PICARD PEANO")
#    print("Iteration ", i, ": ", x)
#    
#newton(2)
#picard_p(2)

#ex4 - metodos de euler e de rk4

#def dC(t,C,T):
#    return -math.exp(-0.5/(T+273)) * C
#
#def dT(t,C,T):
#    return 30*math.exp(-0.5/(T+273)) * C - 0.5 * (T - 20)
#
#def Euler(t,C,T,h):
#    i = 0
#    print("Iteration 0: ",t,C,T)
#    while(t + h < 0.51):
#        i += 1
#        t += h
#        C += dC(t,C,T) * h
#        T += dT(t,C,T) * h
#        print("Iteration ",i,": ",t,C,T)
#    return T
#
#def rk4(t,C,T,h):
#    i = 0
#    print("Iteration 0: ",t,C,T)
#    while(t + h < 0.51):
#        i += 1
#        t += h
#        deltaC_1 = h * dC(t,C,T) 
#        deltaT_1 = h * dT(t,C,T)
#        deltaC_2 = h * dC(t + h/2, C + deltaC_1/2, T + deltaT_1/2)
#        deltaT_2 = h * dT(t + h/2, C + deltaC_1/2, T + deltaT_1/2)
#        deltaC_3 = h * dC(t + h/2, C + deltaC_2/2, T + deltaT_2/2)
#        deltaT_3 = h * dT(t + h/2, C + deltaC_2/2, T + deltaT_2/2)
#        deltaC_4 = h * dC(t + h, C + deltaC_3, T + deltaT_3)
#        deltaT_4 = h * dT(t + h, C + deltaC_3, T + deltaT_3)
#        
#        C += deltaC_1/6 + deltaC_2/3 + deltaC_3/3 + deltaC_4/6
#        T += deltaT_1/6 + deltaT_2/3 + deltaT_3/3 + deltaT_4/6
#        
#        print("Iteration ",i,": ",t,C,T)
#    return T
#
#print("EULER")
#e1 = Euler(0,2.5,25,0.25)
#print("e1: ", e1)
#e2 = Euler(0,2.5,25,0.25/2)
#print("e2: ", e2)
#e3 = Euler(0,2.5,25,0.25/4)
#print("e3: ", e3)
#qc = (e2 - e1) / (e3 - e2)
#print("qc: ", qc)
#er = (e3 - e2)
#print("erro: ", er)
#print("RK4")
#r1 = rk4(0,2.5,25,0.25)
#print("r1: ", r1)

#ex.5 - metodo do gradiente

def f(x,y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x

def fx(x,y):
    return -1.1*y + 14*x - 8

def fy(x,y):
    return -1.1*x + 12

def gradiente(x,y,h):
    xn = x - h * fx(x,y)
    yn = y - h * fy(x,y)
    return f(xn,yn)

print(gradiente(3,1,0.1))
    

import math

#ex2 - metodo de newton

#def f(x,y):
#    return x**2 - y - 1.2
#
#def fx(x,y):
#    return 2*x
#
#def fy(x,y):
#    return -1
#
#def g(x,y):
#    return -x + y**2 - 1
#
#def gx(x,y):
#    return -1
#
#def gy(x,y):
#    return 2*y
#
#def jacobian(x,y):
#    return fx(x,y) * gy(x,y) - fy(x,y) * gx(x,y)
#
#def newton(x,y):
#    print("Iteration 0: ", x, y)
#    for i in range(1,3):
#        x0 = x
#        y0 = y
#        x = x0 - (f(x0,y0) * gy(x0,y0) - g(x0,y0) * fy(x0,y0)) / jacobian(x0,y0)
#        y = y0 - (g(x0,y0) * fx(x0,y0) - f(x0,y0) * gx(x0,y0)) / jacobian(x0,y0)
#        print("Iteration ", i, ": ", x, y)
#    
#newton(1,1)
 
#ex4 - metodo da corda       

#def f(x):
#    return x**7 + 0.5*x - 0.5
#
#def corda(a,b):
#    for i in range(4):
#        xm = (a * f(b) - b * f(a)) / (f(b) - f(a))
#        print("Iteration ", i, ": ", a, b, xm)
#        if(f(a) * f(xm) < 0):
#            a = a
#            b = xm
#        else:
#            a = xm
#            b = b
#
#corda(0,0.8)

#ex5 - metodo de euler r rk4

#def dy(t,y,z):
#    return z
#
#def dz(t,y,z):
#    return 0.5 + t**2 + t * z
#
#def euler(t,y,z,h):
#    print("Iteration 0: ", t, y, z)
#    for i in range(1, 3):
#        t0 = t
#        t = t0 + h
#        y = y + dy(t0,y,z) * h
#        z = z + dz(t0,y,z) * h
#        print("Iteration ", i, ": ", t, y, z)
#        
#def rk4(t,y,z,h):
#    print("Iteration 0: ", t, y, z)
#    for i in range(1, 3):
#        t0 = t
#        t = t0 + h
#        deltay_1 = h * dy(t0,y,z)
#        deltaz_1 = h * dz(t0,y,z)
#        deltay_2 = h * dy(t0 + h/2, y + deltay_1/2, z + deltaz_1/2)
#        deltaz_2 = h * dz(t0 + h/2, y + deltay_1/2, z + deltaz_1/2)
#        deltay_3 = h * dy(t0 + h/2, y + deltay_2/2, z + deltaz_2/2)
#        deltaz_3 = h * dz(t0 + h/2, y + deltay_2/2, z + deltaz_2/2)
#        deltay_4 = h * dy(t0 + h, y + deltay_3, z + deltaz_3)
#        deltaz_4 = h * dz(t0 + h, y + deltay_3, z + deltaz_3)
#        
#        y = y + deltay_1/6 + deltay_2/3 + deltay_3/3 + deltay_4/6
#        z = z + deltaz_1/6 + deltaz_2/3 + deltaz_3/3 + deltaz_4/6
#        
#        print("Iteration ", i, ": ", t, y, z)
#        
#euler(0,0,1,0.25)
#rk4(0,0,1,0.25)

#ex6 - metodos dos trapexios e de simpson

def f(x):
    return math.sqrt(1 + 1.5*math.exp(1.5*x))**2

def simpson(a,b,h):
    total = 0
    n = int((b - a)/h)
    for i in range(1, n, 2):
        total += 4 * f(a + i * h)
    for i in range(2, n, 2):
        total += 2 * f(a + i * h)
    total += f(a) + f(a + n * h)
    total *= h / 3
    return total

def trapezios(a,b,h):
    total = 0
    n = int((b - a)/h)
    for i in range(1,n):
        total += 2 * f(a + i * h)
    total += f(a) + f(a + n * h)
    total *= h / 2
    return total

t1 = trapezios(0,2,0.5)
t2 = trapezios(0,2,0.5/2)
t3 = trapezios(0,2,0.5/4)
qc = (t2 - t1) / (t3 -t2)
er = (t3 - t2) / 3
s1 = simpson(0,2,0.5)
s2 = simpson(0,2,0.5/2)
s3 = simpson(0,2,0.5/4)
qcs = (s2 - s1) / (s3 - s2)
ers = (s3 - s2) / 15
print("TRAPEZIOS")
print("t1: ", t1)
print("t2: ", t2)
print("t3: ", t3)
print("qc: ", qc)
print("erro: ", er)
print("SIMPSON")
print("s1: ", s1)
print("s2: ", s2)
print("s3: ", s3)
print("qc: ", qcs)
print("erro: ", ers)

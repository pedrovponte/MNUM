import math


#-------------------Método da bisseção-------------------#

#def f(x):
#    return x**2-16
#
#def converge(a,b):
#    if f(a)*f(b)<=0:
#        return "Converge"
#    else:
#        return "Nao converge"
#        
#def bissection(a,b):
#    n = 0
#    while(((b-a)/2^n) > 5e-5):
#        m = (a+b)/2
#        if (f(a)*f(m) < 0):
#            b = m
#        else:
#            a = m
#        n += 1
#    return m
#
#print(converge(0,4))
#print(bissection(0,4))


#-------------------Método da corda/ falsa posição-------------------#


#def f(x):
#    return x**4+2*x**3-x-1
#
#def converge(a,b):
#    if(f(a)*f(b) <= 0):
#        return "Converge"
#    else:
#        return "Nao converge"
#
#def corda(a,b):
#    n = 0
#    while(n < 20):
#        m = (a*f(b)-b*f(a))/(f(b)-f(a))
#        if (f(a)*f(m) < 0):
#            b = m
#        else:
#            a = m
#        n += 1
#    return m
#
#print(converge(4,16))
#print(corda(4,16))


#-------------------Método de picard peano-------------------#


#def f(x):
#    return 2*x**2-5*x-3
#
#def derivate(x):
#    return 4*x-5
#
#def converge(x):
#    if (derivate(x) < 1):
#        return "Converge"
#    else:
#        return "Nao converge"
#
#def picardp(guess):
#    x = guess
#    last = 0
#    while(((derivate(x)/(1-derivate(x))) * (x-last)) > 5e-5):
#        last = x
#        x = f(last)
#        print(x)
#    return x
#
#print(converge(1))
#print(picardp(1))


#-------------------Método de Newton-------------------#
    

#def f(x):
#    return x**4-2*x**3-x-1
#
#def derivate(x):
#    return 4*x**3-6*x**2-1
#
#def derivate2(x):
#    return 12*x**2-12*x
#
#def converge(x)
#    if((f(x)*derivate2(x)) >= 0):
#        return "Converge"
#    else:
#        return "Nao converge"
#
#def newton(guess):
#    x = guess
#    last = 0
#    while(((derivate2(x)/(2*derivate(x)))*(last-x)**2) > 5e-5):
#        last = x
#        x = last - (f(x)/derivate(x))
#        print(x)
#    return x
#
#print(converge(1))
#print(newton(1))


#-------------------Método de picard peano para sistemas de equaçoes-------------------#


#def f(x,y):
#    return math.sqrt((x * y + 5 * x - 1) / 2.0)
#
#def g(x,y):
#    return math.sqrt(x + 3 * math.log10(x))
#
#def picardp_sis(x,y):
#    it = 0
#    last_x = x - 10
#    last_y = y - 10
#    while((abs(x-last_x) > 10e-5) & (abs(y-last_y) > 10e-5)):
#        it += 1
#        last_x = x
#        last_y = y
#        x = f(last_x)
#        y = g(last_y)
#        print(x,y)
#    return x,y
#
#print(picardp_sis(2,3))


#-------------------Método de picard peano para sistemas de equaçoes-------------------#


def f(x,y):
    return -x**2 + 1 - y

def g(x,y):
    return -y + 0.7 + x

def derivate_fx(x,y):
    return -2*x

def derivate_fy(x,y):
    return -1

def derivate_gx(x,y):
    return 1

def derivate_gy(x,y):
    return -1

def newton_sis(x0,y0):
    it = 0
    last_x = x0 - 10
    last_y = y0 - 10
    while((abs(x0-last_x) > 10e-5) & (abs(y0-last_y) > 10e-5)):
        it += 1
        last_x = x0
        last_y = y0
        
        jacobian = derivate_fx(last_x,last_y) * derivate_gy(last_x,last_y) - derivate_fy(last_x,last_y) * derivate_gx(last_x,last_y)
        
        x0 = 
        y0 = 









import math

#def f1(x):
#    return x**3+2*x**2+10*x-17
#
#
#def bissecao(a,b):
#    n = 0
#    while(n < 23 ):
#        m = (a + b)/2
#        if(f1(a) * f1(m) < 0):
#            b = m
#        else:
#            a = m
#        n += 1
#        
#    return m
#
#print(bissecao(2.6,4.6))


#def f2(x):
#    return x**3+2*x**2+10*x-17
#
#def derivate(x):
#    return 3*x**2+4*x+10
#
#def newton(guess):
#    last = 0
#    x = guess
#    n = 0
#    while(n<20):
#        last = x
#        x = x - f2(x) / derivate(x)
#        n += 1
#        print(x)
#    return x 
#
#print(float(newton(0)))

#def f3(x,y):
#    return math.sqrt(-y**2 + 6*x - 5)
#
#def f4(x,y):
#    return math.log10(x-1)
#
#def picard_peano_sis(x,y):
#    last_x = x - 10
#    last_y = y - 10
#
#    while((abs(x - last_x) > 10e-5) & (abs(y - last_y) > 10e-5)):
#        last_x = x
#        last_y = y
#        x = f3(x,y)
#        y = f4(x,y)
#        print(x,y)
#    return x,y
#
#print(picard_peano_sis(1.50000,1.3000))

def f5(x,y):
    return y - math.log(x-1)

def derivate_fx(x,y):
    return -1/(x-1)

def derivate_fy(x,y):
    return 1

def g1(x,y):
    return y**2 + (x - 3)**2 - 4

def derivate_gx(x,y):
    return 2 * (x - 3)

def derivate_gy(x,y):
    return 2 * y

def newton_sis(x0,y0):
    last_x = x0 - 10 
    last_y = y0 -10
    
    while((abs(x0 - last_x) > 10e-5) & (abs(y0 - last_y) > 10e-5)):
        last_x = x0
        last_y = y0
        
        jacobian = derivate_fx(last_x,last_y) * derivate_gy(last_x,last_y) - derivate_gx(last_x,last_y) * derivate_fy(last_x,last_y)
        
        x0 = last_x - ((f5(last_x,last_y) * derivate_gy(last_x,last_y) - g1(last_x,last_y) * derivate_fy(last_x,last_y)) / jacobian)
        y0 = last_y - ((g1(last_x,last_y) * derivate_fx(last_x,last_y) - f5(last_x,last_y) * derivate_gx(last_x,last_y)) / jacobian)
        
        print(x0,y0)
        
    return x0,y0

print(newton_sis(1.50000,1.30000))
    



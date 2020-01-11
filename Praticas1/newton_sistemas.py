import math

def f(x,y):
    return 2*x**2-x*y-5*x-1

def derivate_fx(x,y):
    return 4*x-y-5

def derivate_fy(x,y):
    return -x

def g(x,y):
    return x+3*math.log10(x)-y**2

def derivate_gx(x,y):
    return 1+3/x

def derivate_gy(x,y):
    return -2*y

def newton_sis(x0,y0):
    last_x = x0 - 10 
    last_y = y0 - 10
    
    while((abs(x0 - last_x) > 10e-5) & (abs(y0 - last_y) > 10e-5)):
        last_x = x0
        last_y = y0
        
        jacobian = derivate_fx(last_x,last_y) * derivate_gy(last_x,last_y) - derivate_gx(last_x,last_y) * derivate_fy(last_x,last_y)
        
        x0 = last_x - ((f(last_x,last_y) * derivate_gy(last_x,last_y) - g(last_x,last_y) * derivate_fy(last_x,last_y)) / jacobian)
        y0 = last_y - ((g(last_x,last_y) * derivate_fx(last_x,last_y) - f(last_x,last_y) * derivate_gx(last_x,last_y)) / jacobian)
        
        print(x0,y0)
        
    return x0,y0

print(newton_sis(1.46,-1.41))

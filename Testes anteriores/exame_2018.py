import math

#ex1 - newton 2 vars

#def f1(x,y):
#    return math.sin(x+y)-math.exp(x-y)
#
#def f2(x,y):
#    return math.cos(x+y)-x**2*y**2
#
#def f1x(x,y):
#    return math.cos(x+y)-math.exp(x-y)
#
#def f1y(x,y):
#    return math.cos(x+y)+math.exp(x-y)
#
#def f2x(x,y):
#    return -math.sin(x+y)-2*x*y**2
#
#def f2y(x,y):
#    return -math.sin(x+y)-2*x**2*y
#
#def jacobian(x,y):
#    return f1x(x, y) * f2y(x, y) - f1y(x, y) * f2x(x, y)
#def newton(x0,y0):
#    x = x0
#    y = y0
#    for i in range(3):
#        x = x - (f1(x, y) * f2y(x, y) - f1y(x, y) * f2(x, y)) / jacobian(x, y)
#        y = y - (f1x(x, y) * f2(x, y) - f2x(x, y) * f1(x, y)) / jacobian(x, y)
#        print("x: ", x, "y: ", y)
#        
#newton(0.5,0.25)

#ex4 - euler 2 ordem

def dy(x,y,z):
    return z

def dz(x,y,z):
    return -7*z - 4*y

def euler(x,y,z,h):
    print("Iteration 1: ",x,y,z)
    for i in range(2,5,1):
        x += h
        y += dy(x,y,z) * h
        z += dz(x,y,z) * h
        print("Iteration ",i,": ",x,y,z)
        
euler(0.4,2,1,0.2)  

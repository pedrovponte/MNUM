import math

#---------------------Ex.1b---------------------------#

def ex_1b(b):
    return 1/b

print(ex_1b(0.694))

#---------------------Ex.3c---------------------------#

def fx(x,y):
    return (x**2+0.3)/(2*x+1)

def fy(x,y):
    return (x**2+1.4*x+1)/(2*x+1)

def newton(x,y):
    last_x = x - 10
    last_y = y - 10
    while((abs(x-last_x)>10e-3) & (abs(y-last_y)>10e-3)):
        last_x = x
        last_y = y
        
        x = fx(last_x,last_y)
        y = fy(last_x,last_y)
        
        print(x,y)
    return x,y

print(newton(-2,0))

#---------------------Ex.3d---------------------------#

def f1(x,y):
    return -math.sqrt(1-y)

def g1(x,y):
    return 0.7+x

def f2(x,y):
    return y-0.7

def g2(x,y):
    return 1-x**2

def picard_p1(x,y):
    last_x = x - 10
    last_y = y - 10
    for n in range(20000):
        n += 1
        last_x = x
        last_y = y
        x = f1(last_x,last_y)
        y = g1(last_x,last_y)
        print("n: ", n,x,y)
        if((last_x == x) & (last_y == y)):
            break
    return x,y

def picard_p2(x,y):
    last_x = x - 10
    last_y = y - 10
    for n in range(20000):
        n += 1
        last_x = x
        last_y = y
        x = f2(last_x,last_y)
        y = g2(last_x,last_y)
        print("n: ", n,x,y)
        if((last_x == x) & (last_y == y)):
            break
    return x,y
    
print(picard_p1(0.0,0.5))
print("\n")
print(picard_p2(0.0,0.5))
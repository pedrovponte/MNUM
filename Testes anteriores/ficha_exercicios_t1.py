import math

def f(x):
    return math.sin(10*x)+math.cos(3*x)

def derivate(x):
    return 10*math.cos(10*x)-3*math.sin(3*x)

def f1(x):
    return math.e**(-x)

def f2(x,y):
    return x+y-3

def f2x(x,y):
    return 1

def f2y(x,y):
    return 1

def g2(x,y):
    return x**2+y**2-9

def g2x(x,y):
    return 2*x

def g2y(x,y):
    return 2*y

def bissection(a,b):
    n=0
    while((abs((b-a)/b) > 0.005) or ((abs(a-b)/a) > 0.005)):
        n += 1
        m = (a+b)/2
        if(f(a)*f(m) < 0):
            b = m
        else: 
            a = m
        print("N:",n," ",a,b)  
    return m

def corda(a,b):
    n = 0
    while((abs((b-a)/b) > 0.005) or ((abs(a-b)/a) > 0.005)):
        n += 1
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(m) < 0):
            b = m
        else:
            a = m
        print("N:",n," ",a,b)
    return m

def newton(guess):
    x = guess
    last = 0
    n = 0
    while((abs(x-last)/x) > 0.005):
        n += 1
        last = x
        x = last - f(last)/derivate(last)
        print("N:",n," ",x)
    return x

def picardp(guess):
    last = 0
    x = guess
    n = 0
    while(abs(x-last)>10**-5):
        n += 1
        last = x
        x = f1(last)
        print("N:",n," ",x)
    return x

def newton_sis(x,y):
    n = 0
    last_x = x - 10
    last_y = y - 10
    while(((abs(x-last_x)/x) > 0.005) or ((abs(y-last_y)/y) > 0.005)):
        n += 1
        last_x = x
        last_y = y
        
        jacobian = f2x(last_x,last_y)*g2y(last_x,last_y)-g2x(last_x,last_y)*f2y(last_x,last_y)
        
        x = last_x - ((f2(last_x,last_y)*g2y(last_x,last_y)-f2y(last_x,last_y)*g2(last_x,last_y))/jacobian)
        y = last_y - ((f2x(last_x,last_y)*g2(last_x,last_y)-g2x(last_x,last_y)*f2(last_x,last_y))/jacobian)
        
        print("N:",n," ",x,y)
    return x,y


#print(bissection(3.24,3.3))
#print("\n")
#print(bissection(5.6,5.7))
#print("\n")
#print(corda(3.24,3.3))
#print("\n")
#print(corda(5.6,5.7))
#print("\n")
#print(newton(3.2))
#print("\n")
#print(newton(5.6))
#print(picardp(0.5))
#print("\n")
#print(picardp(1.1))
#print("\n")
#print(newton_sis(4,1))

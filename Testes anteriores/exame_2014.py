import math

#ex 2 - metodo de newton

#def f(x):
#    return -x + 40*math.cos(math.sqrt(x)) + 3
#
#def dfx(x):
#    return -1 - (20*math.sin(math.sqrt(x)))/(math.sqrt(x))
#
#def newton(guess):
#    x = guess
#    print("1: ",x,f(x))
#    for i in range(2):
#        x = x - f(x) / dfx(x)
#        print(i, ": ",x,f(x))
#    
#newton(1.7)

#ex 5 - regra aurea

def f(x):
    return 5*math.cos(x)-math.sin(x)

def aurea(x1,x2):
    b = (math.sqrt(5) - 1)/2
    a = b*b
    for i in range(3):
        x3 = x1 + a * (x2 - x1)
        x4 = x1 + b * (x2 - x1)
        print("x: ", x1,x2,x3,x4)
        print("f(x): ", f(x1),f(x2),f(x3),f(x4))
        if(f(x3) < f(x4)):
            x2 = x4
            x1 = x1
        else:
            x1 = x3
            x2 = x2
        
        
aurea(2,4)
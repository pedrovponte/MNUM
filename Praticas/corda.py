import math

def f(x):
    return x**4+2*x**3-x-1

def corda(a,b,n):
    for i in range(n):
        m = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if(f(m) * f(a) > 0):
            a = m
        else:
            b = m
    return m

print(float(corda(0,1,10)))
        
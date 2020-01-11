import math

def f(x):
    return pow(math.sin(x), 2)

def tercos(a,b,prec):
    while(abs(b - a) > prec):
        prop = (b - a) / 3
        c = a + prop
        d = b - prop
        if(f(c) > f(d)):
            a = c
        else:
            b = d
    if(a == c):
        return [c, d, b]
    else:
        return [a, c, d]
    
lista = tercos(3, 6, 0.001)
print(lista)
def BabylonianAlgorithm(number):
    if(number == 0):
        return 0;

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;
print(BabylonianAlgorithm(0.3));


def f(x):
    return x*x-16


def bissecao(a,b):
    n = 0
    while(n < 23 ):
        m = (a + b)/2
        if(f(a) * f(m) < 0):
            b = m
        else:
            a = m
        n += 1
        
    return m

print(bissecao(0,1))

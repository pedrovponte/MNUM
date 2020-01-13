import math

#ex1 - metodo de euler

#def dT(t,T):
#    return -0.25 * (T - 37)
#
#def euler(t,T,h):
#    for i in range(2):
#        t_anterior = t
#        t = t + h
#        T = T + h * dT(t_anterior,T)
#    return T
#
#print(euler(5,3,0.4))

#ex4.2 - metodo picard-peano

#def f(x):
#    return 2*math.log(2*x)
#
#def picard_p(x):
#    print("Iteration 0: ",x)
#    x_anterior = x
#    x = f(x_anterior)
#    print("Iteration 1: ",x)
#
#picard_p(1.1)  

#ex5 - metodos dos trapezios e de simpson

#def f(x):
#    return math.sqrt(1 + (2.5*math.exp(2.5*x))**2)
#
#def trapezios(a,b,h):
#    total = 0
#    n = int((b - a) / h)
#    for i in range(1,n):
#        total += 2 * f(a + i * h)
#    total += f(a) + f(a + n * h)
#    total *= h/2
#    return total
#
#def simpson(a,b,h):
#    total = 0
#    n = int((b - a) / h)
#    for i in range(1,n,2):
#        total += 4 * f(a + i * h)
#    for i in range(2,n,2):
#        total += 2 * f(a + i * h)
#    total += f(a) + f(a + n * h)
#    total *= h/3
#    return total
#
#t1 = trapezios(0,1,0.125)
#t2 = trapezios(0,1,0.125/2)
#t3 = trapezios(0,1,0.125/4)
#qc = (t2 - t1) / (t3 -t2)
#er = (t3 - t2) / 3
#s1 = simpson(0,1,0.125)
#s2 = simpson(0,1,0.125/2)
#s3 = simpson(0,1,0.125/4)
#qcs = (s2 - s1) / (s3 - s2)
#ers = (s3 - s2) / 15
#print("TRAPEZIOS")
#print("t1: ", t1)
#print("t2: ", t2)
#print("t3: ", t3)
#print("qc: ", qc)
#print("erro: ", er)
#print("SIMPSON")
#print("s1: ", s1)
#print("s2: ", s2)
#print("s3: ", s3)
#print("qc: ", qcs)
#print("erro: ", ers)

#ex7 - metodo da bissecao

def f(x):
    return x**3 - 10 * math.sin(x) + 2.8

def bissecao(a,b):
    print("Iteration 0: ", a, b)
    for i in range(1,3):
        m = (a + b) / 2
        if(f(a) * f(m) < 0):
            a = a
            b = m
        else:
            b = b
            a = m
        print("Iteration ", i, ": ", a, b)
    return m

print(bissecao(1.5,4.2))
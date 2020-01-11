import math
from copy import deepcopy

#ex1 - Método de Newton

#def f(x):
#    return (x-2.6) + math.pow(math.cos(x+1.1),3)
#
#def derivate(x):
#    return 1 - 3*pow(math.cos(x+1.1),2)*math.sin(x+1.1)
#
#def newton(guess):
#    x = guess
#    x = x - f(x) / derivate(x)
#    return x
#
#r = newton(1.8)
#print(r)  #answer: 7.10525

#ex2 - derivada da 1a expressao: m*(x^(m-1))
#    - derivada da 2a expressao: R*m*(x^(-m-1))
#    A derivada da 2a expressao e mais complexa do que a da 1a, pelo que vai obrigar a fazer mais cálculos para a calcular,
#   pelo que o risco de haver erros de arredondamentos/truncaçao nos cálculos é maior neste caso. Deste modo, 
#    deve-se escolher a 1a expressao.

#ex4 - secçao aurea

#def g(x):
#    return 5*math.cos(x)-math.sin(x)
#
#def aurea(x1,x2):
#    b = (math.sqrt(5) - 1) / 2
#    a = b * b
#    print(x1,x2,x3,x4)
#    print(g(x1),g(x2),g(x3),g(x4))
#    for i in range(3):
#        x3 = x1 + a * (x2 - x1)
#        x4 = x1 + b * (x2 - x1)
#        print(i,x3,x4)
#        
#        if(g(x3) < g(x4)):
#            x1 = x1
#            x2 = x4
#            
#        else:
#            x1 = x3
#            x2 = x2
#            
#        print("x: ", x1,x2,x3,x4)
#        print("g: ",g(x1),g(x2),g(x3),g(x4))
#        
#
#aurea(2,4)

#ex5 - rk4

def f(t,x):
    return math.sin(x)+math.sin(2*t)

def rk4(t,x,h):
    print("t: ", t, "x: ", x)
    while (t + h < 1.51):
        t_anterior = t
        t = t_anterior + h
        delta1 = h * f(t_anterior, x)
        delta2 = h * f(t_anterior + h/2, x + delta1/2)
        delta3 = h * f(t_anterior + h/2, x + delta2/2)
        delta4 = h * f(t_anterior + h, x + delta3)
        
        x = x + delta1/6 + delta2/3 + delta3/3 + delta4/6
        
        print("t: ", t, "x: ", x)
    return x
    


y1 = rk4(1,1,0.5)
print()
y2 = rk4(1,1,0.25)
print()
y3 = rk4(1,1,0.125)
print()

quociente = (y2 - y1) / (y3 - y2)
print("qc: ", quociente)

#ex6 - trapezios


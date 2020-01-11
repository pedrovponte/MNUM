import math

#ex2 - metodo picard-peano

#def f(x):
#    return 2*math.log(2*x)
#    
#def picard(guess):
#    x = guess
#    print("0: ", x)
#    x_anterior = x
#    x = f(x_anterior)
#    print("1: ", x)
#
#picard(0.9)

#ex3 - rk4

#def f(t,x):
#    return math.sin(x) + math.sin(2*t)
#
#def rk4(t,x,h):
#    while(t + h < 1.51):
#        t_anterior = t
#        t += h
#        delta1 = h * f(t_anterior,x)
#        delta2 = h * f(t_anterior + h/2, x + delta1/2)
#        delta3 = h * f(t_anterior + h/2, x + delta2/2)
#        delta4 = h * f(t_anterior + h, x + delta3)
#        
#        x = x + delta1/6 + delta2/3 + delta3/3 + delta4/6
#        print("t: ",t,"x: ", x)
#    return x
#        
#r1 = rk4(1,0,0.5)
#r2 = rk4(1,0,0.5/2)
#r3 = rk4(1,0,0.5/4)
#
#qc = (r2 - r1) / (r3 - r2)
#print("qc: ", qc)


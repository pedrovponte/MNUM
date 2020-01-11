import math

#def f(x):
#    return math.e**(0.7*x) - x**2 - 0.5
#
#def bissecao(a,b):
#    n = 0
#    print(a,b)
#    print(f(a),f(b))
#    while(n < 3):
#        m = (a + b)/2
#        print("m = ", m)
#        print("f(m) = ", f(m))
#        if(f(a) * f(m) < 0):
#            b = m
#        else:
#            a = m
#        print("a = ", a)
#        print("b = ", b)
#        print("f(a) = ", f(a))
#        print("f(b))= ", f(b))
#        n += 1
#    return a,b
#
#print(bissecao(-1,0))

#def f1(x,y):
#    return x**2 - y - 1.2
#
#def df1x(x,y):
#    return 2*x
#
#def df1y(x,y):
#    return -1
#
#def g(x,y):
#    return -x + y**2 - 0.5
#
#def dgx(x,y):
#    return -1
#
#def dgy(x,y):
#    return 2*y
#
#def newton_sis(x0,y0):
#    last_x = x0 - 10
#    last_y = y0 - 10
#    
#    while((abs(x0 - last_x) > 10e-5) & (abs(y0 - last_y) > 10e-5)):
#        last_x = x0
#        last_y = y0
#        
#        jacobian = df1x(last_x,last_y) * dgy(last_x,last_y) - dgx(last_x,last_y)*df1y(last_x,last_y)
#        
#        x0 = last_x - ((f1(last_x,last_y) * dgy(last_x,last_y) - g(last_x,last_y) * df1y(last_x,last_y)) / jacobian)
#        y0 = last_y - ((g(last_x,last_y) * df1x(last_x,last_y) - f1(last_x,last_y) * dgx(last_x,last_y)) / jacobian)
#        
#        print(x0,y0)
#        
#    return x0,y0
#
#newton_sis(1.10000,1.10000)
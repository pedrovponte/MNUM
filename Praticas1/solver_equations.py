import math

def f(x):
    return 2*x**2-5*x-2

def bissec(a,b,p):
    while abs(b - a) > p:
        m = (b + a) / 2
        if f(a)*f(m)<0:
            b = m
        else:
            a = m
#        print (a,m,b,f(m))
    return (b+a)/2

def equation_solver(a, b, c):
    m = math.pow(b,2) - 4*a*c
    result = []
    
    if a == 0:
         x3 = -c/b
         result = [x3]
        
    if m >= 0:
        x1 = (-b + math.sqrt(m))/(2*a)
        x2 = (-b - math.sqrt(m))/(2*a)
        if m == 0:
            result = [x1]
            
        if m > 0:
            result = [x1, x2]
            result = sorted(result)
            
    elif m < 0:
        result = []
        
    return result

y = bissec(2.8,2.9,10**(-15))
z = bissec(-0.5,-0.3,10**(-15))

#print(y)
#print(z)

#print(f(bissec(2.8,2.9,10**(-15))))
#print(f(bissec(-0.5,0,10**(-15))))

res = equation_solver(2,-5,-2)
ea1 = abs(res[0]-z)
ea2 = abs(res[1]-y)
#print(ea1)
#print(ea2)

def false_position_method(a,b,precision):
    rr=b
    rr1=a
    while(abs(b-a) > precision):
        rr = (a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(rr)<=0):
            b = rr
            rr1=(a*f(b)-b*f(a)/2)/(f(b)-f(a)/2)
        else:
            a = rr1
            rr1=(a*f(b)/2-b*f(a))/(f(b)/2-f(a))
    return rr

print(false_position_method(1,10,0.1))
print(false_position_method(-0.5,0,0.15))


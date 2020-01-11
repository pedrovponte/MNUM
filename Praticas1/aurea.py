import math

def f(x):
    return pow(math.sin(x), 2)

def aurea_min(x1, x2, error):
    b = (math.sqrt(5) - 1) / 2
    a = b * b
    while(abs(x1 - x2) > error):
        x3 = x1 + a * (x2 - x1)
        x4 = x1 + b * (x2 - x1)
        
        if(f(x3) < f(x4)):
            x1 = x1
            x2 = x4
            
        else:
            x1 = x3
            x2 = x2
    
    return [x1,x2,x3,x4]

def aurea_max(x1,x2,error):
    b = (math.sqrt(5) - 1) / 2
    a = b * b
    while(abs(x1 - x2) > error):
        x3 = x1 + a * (x2 - x1)
        x4 = x1 + b * (x2 - x1)
        
        if(f(x3) > f(x4)):
            x1 = x1
            x2 = x4
        
        else:
            x1 = x3
            x2 = x2
    
    return [x1,x2,x3,x4]
        

j = aurea_min(-1, 0, 0.001)
print("aurea min: ", j)
k = [f(i) for i in j]
print(j[(k.index(min(k)))])
print(aurea_max(-1, 0, 0.001))
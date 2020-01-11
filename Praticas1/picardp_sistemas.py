import math

def f1(x,y):
    return math.sqrt((x * y + 5 * x - 1) / 2.0)

def f2(x,y):
    return -math.sqrt(x + 3 * math.log10(x))

def picard_peano_sistemas(x,y):
   
   it = 0
   last_x = x - 10
   last_y = y - 10
   
   while((abs(x - last_x) > 10e-7) & (abs(y - last_y) > 10e-7)):
       it += 1
       last_x = x
       last_y = y
       x = f1(x,y)
       y = f2(x,y)
       print(x,y)
   return x,y

print("Resultado: ", picard_peano_sistemas(3.5,2.3))
   

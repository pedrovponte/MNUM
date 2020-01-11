def f(x):
    return x**4-2*x**3-x-1

def derivate(x):
    return 4*x**3-6*x-1

def derivate2(x):
    return 12*x**2-6


#def newton(x,n):
#    last = None
#    while(n and (not last or abs(last-x) >= 1e-5)):
#        last=x
#        x=x-f(x)/derivate(x)
#        n -= 1
#        print(x)
#    return x


def newton(guess):
    x = guess
    for i in range(10):
        x = x - f(x) / derivate(x)
        i += 1
        print(x)
    return x 

def converge(guess):
    if(f(guess)*derivate2(guess) < 1):
        return "Converge"
    else:
        return "Nao converge"


guess = float(input("Guess: "))

print(converge(guess))
print("Solution: %.20f" % newton(guess))



        
        
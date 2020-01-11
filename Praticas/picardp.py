def f(x):
    return 2*x**2-5*x-3

def picardp(guess):
    x = guess
    last = 0
    while(abs(x - last) >= 1e-5):
        last = x
        x = f(last)
        print(x)
    return x

guess = float(input("Guess: "))

print("Solution: " % picardp(guess))


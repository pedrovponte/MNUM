def temp(t):
    return -0.25*(t - 45)

def Euler_temp(T, t, h):
    for i in range(2):
        T += h * temp(T)
    return T

t1 = Euler_temp(23, 1, 0.4)
print(t1)
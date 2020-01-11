import math

def dC(T,C):
    return -math.pow(math.e, -0.1 / (T + 273)) * C

def dT(C,T):
    return 15.0 * math.pow(math.e, -0.1 / (T + 273)) * C - 0.1 * (T - 20)

def Euler(C, T, h, t):
    print("EULER: ")
    print("t: ", t, "C: ", C)
    print("t: ", t, "T: ", T)
    for i in range(8):
        T_anterior = T
        C_anterior = C
        t = t + h
        C += h * dC(T_anterior, C_anterior)
        T += h * dT(C_anterior, T_anterior)
        print("t: ", t, "C: ", C)
        print("t: ", t, "T: ", T)
    return C

def RK4(C, T, h, t):
    print("t: ", t, "C: ", C)
    print("t: ", t, "T: ", T)
    for i in range(2):
        T_anterior = T
        C_anterior = C
        t = t + h
        delta_1C = h * dC(T_anterior, C_anterior)
        delta_1T = h * dT(C_anterior, T_anterior)
        delta_2C = h * dC(T_anterior + h/2, C_anterior + delta_1C / 2)
        delta_2T = h * dT(C_anterior + h/2, T_anterior + delta_1T / 2)
        delta_3C = h * dC(T_anterior + h/2, C_anterior + delta_2C / 2)
        delta_3T = h * dT(C_anterior + h/2, T_anterior + delta_2T / 2)
        delta_4C = h * dC(T_anterior + h, C_anterior + delta_3C / 2)
        delta_4T = h * dT(C_anterior + h, T_anterior + delta_3T / 2)
        
        T += delta_1T / 6 + delta_2T / 3 + delta_3T / 3 + delta_4T / 6
        C += delta_1C / 6 + delta_2C / 3 + delta_3C / 3 + delta_4C / 6
        
        print("t: ", t, "C: ", C)
        print("t: ", t, "T: ", T) 
  

s1 = Euler(2.00000, 20.00000, 0.25, 0.5)
print("s1: ", s1)
s2 = Euler(2.00000, 20.00000, 0.1250, 0.5)
print("s2: ", s2)
s3 = Euler(2.00000, 20.00000, 0.0625, 0.5)    
print("s3: ", s3)
QC = (s2 - s1) / (s3 - s2)
print("QC: ", QC)
erro = (s3 - s2) / 3
print("erro: ", erro)
s2 = RK4(2.00000, 20.00000, 0.25, 0.5)

def g(t):
    return -0.25*(t - 64)

def Euler1(T, h, t):
    for i in range(2):
        T += h * g(T)
        print(T)


t1 = Euler1(0, 0.5, 4)
    
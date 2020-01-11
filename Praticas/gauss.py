import copy

m = [[3,2,3,16],
     [2,5,1,15],
     [4,2,3,17]]

mc = copy.deepcopy(m)
dimV = len(m)

def gauss(m):
    for diag in range(dimV):
        pivot = m[diag][diag]
        for col in range(dimV + 1):
            m[diag][col] /= pivot
        for lin in range(diag + 1, dimV):
            pivot2 = m[lin][diag]
            for col in range(diag, dimV + 1):
                m[lin][col] -= m[diag][col] * pivot2
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            factor = m[lin][diag]
            for col in range(dimV, diag - 1, -1):
                m[lin][col] -= m[diag][col] * factor
    return m

print(gauss(m))
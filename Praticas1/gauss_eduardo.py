import math
from copy import deepcopy

def solveMatrix(M, sol):
    M2 = deepcopy(M)
    for d in range(len(M2)):
        for c in range(len(M2[0])-1,-1,-1):
            M2[d][c] = (M2[d][c]*1.0) / (M2[d][d]*1.0)
        for lin in range(d+1,len(M2)):
            for col in range(len(M2[d])-1,0-1,-1):
                M2[lin][col] = M2[lin][col] - M2[d][col]*M2[lin][d]
                
    print("MATRIX:")
    for i in M2 : print(i)

    for d in range(len(M2)-1, -1, -1):
        factor = 0
        csum = 0
        for c in range(len(M2[0])-1):
            if(c == d):
                factor = M2[d][c]
            else:
                csum += M2[d][c] * sol[c] 
        sol[d] = (M2[d][len(M2[d])-1] - csum)/factor

    print()
    print("SOLUTION:")
    print(sol)

def calcResidue(M,sol,resd):
    for l in range(len(M)):
        csum = 0
        for c in range(len(M[l])-1):
            csum += sol[c]*M[l][c]
        resd[l] = M[l][len(M[l])-1] - csum

    print()
    print("RESIDUE:")
    print(resd)
    print()

def ExternStability(M,sol,resd,dA,dB):
    print("EXTERNAL STABILITY: ")
    print()
    DA = [[ dA for i in range(3)] for i in range(3)]
    
    for i in range(len(DA)):
        for j in range(len(DA[i])):
            DA[i][j] = DA[i][j]*sol[j]

    for i in range(len(sol)):
        sol[i] = sum(DA[i])

    b = [dB - i for i in sol ]

    M3 = deepcopy(M)

    for i in range(len(M3)):
        M3[i][len(M3[i])-1] = b[i]
    solveMatrix(M3,sol)
    calcResidue(M3,sol,resd)
    
def TestSolution(M,sol,resd, count):
    for i in range(count):
        print("###########################", i + 1, "###########################")
        print("SOLUTION to test:")
        print(sol)

        calcResidue(M,sol,resd)

        M4 = deepcopy(M)

        for i in range(len(M4)):
            M4[i][len(M4[i])-1] = resd[i]

        sol2 = [0,0,0]

        solveMatrix(M4,sol2)

        finalSol = [sol[i] + sol2[i] for i in range(len(sol))]

        print()
        print("FINAL SOLUTION: ")
        print(finalSol)

        calcResidue(M,finalSol,resd)
        sol = finalSol

M = [[3,2,3,16],
     [2,5,1,15],
     [4,2,3,17]]


M1 = [[9,1,5,25],
     [1,4,6,16],
     [2,9,7,29]]

sol = [2,3,6]
resd = [0,0,0]

solveMatrix(M,sol)
calcResidue(M,sol,resd)

ExternStability(M,sol,resd,0.1,0.1)

#TestSolution(M,[1,2,2.9],resd,2)

# resolver de novo mas b = resd
# resolver de novo mas ... b = something more

        










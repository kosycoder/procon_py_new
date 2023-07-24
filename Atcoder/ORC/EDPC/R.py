from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

MOD = int(1e9+7)

N, K = map(int,input().split())
a = []
for i in range(N):
    atmp = input().split()
    atmp = [int(val) for val in atmp]
    a.append(atmp)

def matrixmulmod(A, B):
    C = []
    for i in range(N):
        Ctmp = []
        for j in range(N):
            c = 0
            for k in range(N):
                c += A[i][k]*B[k][j]
                c %= MOD
            Ctmp.append(c)
        C.append(Ctmp)
    return C

def matrixpowmod(M, k, MOD):
    if k == 1:
        return M
    
    if k % 2 == 0:
        Mtmp = matrixpowmod(M, k//2, MOD)
        return matrixmulmod(Mtmp, Mtmp)
    else:
        return matrixmulmod(M, matrixpowmod(M, k-1, MOD))

X = matrixpowmod(a, K, MOD)
DEBUG(X)
ans = 0
for i in range(N):
    for j in range(N):
        ans += X[i][j]
        ans %= MOD

print(ans)

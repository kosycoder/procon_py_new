import bisect

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

N = int(input())
MOD = 1000

def matmul(A, B):
    C = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                C[i][j] = (C[i][j]+A[i][k]*B[k][j])
    
    return C

def matpow(A, n):
    B = [[0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        B[i][i] = 1
    
    while n > 0:
        if (n & 1):
            B = matmul(B, A)
        A = matmul(A, A)
        n >>= 1
    
    return B

def solve():
    A = [[0] * 2 for _ in range(2)]
    A[0][0] = 3
    A[0][1] = 5
    A[1][0] = 1
    A[1][1] = 3
    A = matpow(A, N)
    ans = (A[0][0] * 2 + MOD - 1) % MOD
    if ans <= 99:
        print(0,end="")
        print(ans)
    else:
        print(ans)

solve()

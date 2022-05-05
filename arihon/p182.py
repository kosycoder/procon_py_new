def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

M = int(1e4)

def matmul(A, B):
    C = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                C[i][j] = (C[i][j]+A[i][k]*B[k][j]) % M
    
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
    n = int(input())
    A = [[0] * 3 for _ in range(3)]
    A = [[2, 1, 0], [2, 2, 2], [0, 1, 2]]
    A = matpow(A, n)
    print(A[0][0])

solve()

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
    n = int(input())
    k = int(input())
    M = int(input())
    A = []
    ans = []
    anstmp = []
    for i in range(n):
        A.append(input_intarray())
    print(A)

    B = [[0] * (2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]
        B[n+i][i] = 1
        B[n+i][n+i] = 1
    B = matpow(B,k+1)
    for i in range(n):
        for j in range(n):
            a = B[n+i][j] % M
            if i == j:
                a = (a + M - 1) % M
            if j + 1 == n:
                anstmp.append(a)
                ans.append(anstmp)
                anstmp = []
            else:
                anstmp.append(a)
    print(ans)
solve()

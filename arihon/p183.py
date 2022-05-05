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
    k = int(input())
    m = int(input())
    G = [[0] * n for _ in range(n)]
    for _ in range(m):
        x, y = map(int,input().split())
        x -= 1
        y -= 1
        G[x][y] = 1
    G = matpow(G, k)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += G[i][j]
    print(ans)
    
solve()

# 4
# 2
# 5
# 1 2
# 1 3
# 2 3
# 3 4
# 4 1

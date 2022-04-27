import math

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

N, Q = map(int,input().split())
A = list(map(int,input().split()))
T = list(map(int,input().split()))
L = list(map(int,input().split()))
R = list(map(int,input().split()))
X = list(map(int,input().split()))
MAX_N = int(1e5)

bit0 = [0] * (MAX_N + 1)
bit1 = [0] * (MAX_N + 1)

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

def solve():
    BIT = BinaryIndexedTree(N)

    for i in range(1,N+1):
        BIT.add(bit0, i, A[i])
    
    for i in range(Q):
        if T[i] == "C":
            BIT.add(bit0, L[i], -X[i]*(L[i] - 1))
            BIT.add(bit1, L[i], X[i])
            BIT.add(bit0, R[i] + 1, X[i] * R[i])
            BIT.add(bit1, R[i] + 1, -X[i])
        else:
            res = 0
            res += sum(bit0, R[i]) + sum(bit1, R[i]) * R[i]
            res -= sum(bit0, L[i] - 1) + sum(bit1, L[i] - 1) * (L[i] - 1)
            print(res)

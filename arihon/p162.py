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

N = int(input())
A = list(map(int,input().split()))

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

BIT = BinaryIndexedTree(N)
ans = 0
for j in range(N):
    ans += j - BIT.sum(A[j])
    BIT.add(A[j], 1)

print(ans)

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

N = int(input())
h = input().split()
h = [int(i)-1 for i in h]
a = input().split()
a = [int(i) for i in a]

n_ = 1
while n_ < N:
    n_ *= 2
dp = [0] * (2*n_-1)

def update(k, a):
    k += n_ - 1
    dp[k] = a
    while k > 0:
        k = int((k-1)/2)
        dp[k] = max(dp[2*k+1], dp[2*k+2])

def query(a, b, k, l, r):
    if r<=a or b<=l:
        return 0
    if a<=l and r<=b:
        return dp[k]
    else:
        vl = query(a, b, 2*k+1, l, int((l+r)/2))
        vr = query(a, b, 2*k+2, int((l+r)/2), r)
        return max(vl, vr)

for i in range(0,N):
    q = query(0,h[i],0,0,n_)
    update(h[i], max(q, q + a[i]))

print(query(0,n_,0,0,n_))

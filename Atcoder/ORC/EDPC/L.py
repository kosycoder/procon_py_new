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

def solve(l, r):
    if flg[l][r]:
        return dp[l][r]
    
    flg[l][r] = True

    if l==r:
        dp[l][r] = a[l]
    else:
        dp[l][r] = max(a[l]-solve(l+1,r),a[r]-solve(l,r-1))
    return dp[l][r]

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N = int(input())
a = [-1]
atmp = input().split()
atmp = [int(i) for i in atmp]
for valatmp in atmp:
    a.append(valatmp)

dp = [[0] * (N+1) for _ in range(N+1)]
flg = [[False] * (N+1) for _ in range(N+1)]

print(solve(1,N))

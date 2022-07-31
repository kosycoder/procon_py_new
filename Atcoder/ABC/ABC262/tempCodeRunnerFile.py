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

DEBUGFLG = True
MOD = 998244353

N = int(input())
a = [-1]
atmp = input().split()
atmp = [int(i) for i in atmp]
for valatmp in atmp:
    a.append(valatmp)

maxval = 10
ans = 0
for n in range(1,N+1):
    dp = [[[0]*(maxval+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(0,maxval+1):
                dp[i][j][k] += dp[i-1][j][k]
                dp[i][j][k] %= MOD
                dp[i][j][(k+a[i])%n] += dp[i-1][j-1][k]
                dp[i][j][(k+a[i])%n] %= MOD
    ans += dp[N][n][0]
    ans %= MOD
    DEBUG(dp)

print(ans)

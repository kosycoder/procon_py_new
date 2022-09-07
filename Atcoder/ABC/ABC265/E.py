from collections import defaultdict

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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
MOD = 998244353

DEBUGFLG = False
N, M = map(int,input().split())
A, B, C, D, E, F = map(int,input().split())
XY = defaultdict(dict)
for _ in range(M):
    Xtmp, Ytmp = map(int,input().split())
    XY[Xtmp][Ytmp] = 1

dp = [[[0] * (N+5) for _ in range(N+5)] for _ in range(N+5)]
dp[0][0][0] = 1
for i in range(N+1):
    for j in range(N+1):
        for k in range(N-i-j+1):
            if not((i+1)*B+j*D+k*F in XY[(i+1)*A+j*C+k*E]):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= MOD
            if not(i*B+(j+1)*D+k*F in XY[i*A+(j+1)*C+k*E]):
                dp[i][j+1][k] += dp[i][j][k]
                dp[i][j+1][k] %= MOD
            if not(i*B+j*D+(k+1)*F in XY[i*A+j*C+(k+1)*E]):
                dp[i][j][k+1] += dp[i][j][k]
                dp[i][j][k+1] %= MOD

ans = 0
for i in range(N+1):
    for j in range(N+1):
        if N-i-j>=0:
            ans += dp[i][j][N-i-j]
            ans %= MOD
print(ans)

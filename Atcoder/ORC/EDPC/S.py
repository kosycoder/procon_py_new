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

MOD = int(1e9+7)

K = input()
D = int(input())
N = len(K)

dp = [[[0] * 110 for _ in range(2)] for _ in range(10010)]

dp[0][0][0] = 1
for i in range(N):
    for j in range(D):
        for k in range(10):
            dp[i+1][1][(j+k)%D] += dp[i][1][j]
            dp[i+1][1][(j+k)%D] %= MOD
        for k in range(int(K[i])):
            dp[i+1][1][(j+k)%D] += dp[i][0][j]
            dp[i+1][1][(j+k)%D] %= MOD
        dp[i+1][0][(j+int(K[i]))%D] += dp[i][0][j]
        dp[i+1][0][(j+int(K[i]))%D] %= MOD

ans = (dp[N][0][0] + dp[N][1][0] - 1 + MOD) % MOD
print(ans)

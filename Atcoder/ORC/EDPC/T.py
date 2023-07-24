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

N = int(input())
s = input()

dp = [[0] * (N+5) for _ in range(N+5)]
cum = [0] * (N+1)

for j in range(N):
    dp[1][j] = 1

for i in range(2,N):
    for j in range(1,N-i+3):
        cum[j] = (cum[j-1]+dp[i-1][j])%MOD
    if s[i-1] == "<":
        for j in range(0,N-i+1):
            dp[i][j] = (cum[N-i+2]-cum[j+1]+MOD)%MOD
    else:
        for j in range(0,N-i+1):
            dp[i][j] = cum[j+1]

ans = dp[N][0]
print(ans)
print(dp)

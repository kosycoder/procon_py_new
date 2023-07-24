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
a = []
for i in range(N):
    atmp = input().split()
    atmp = [int(i) for i in atmp]
    a.append(atmp)

#TLE:O(N*N*2^N)
# dp = [[0] * (1<<N) for _ in range(N+1)]
# dp[0][0] = 1
# for i in range(1,N+1):
#     for j in range(0,1<<N):
#         for k in range(0,N):
#             if (j>>k)&1 == 1 and a[i-1][k] == 1:
#                 dp[i][j] += dp[i-1][j^(1<<k)] # i 番目の男性とk番目の女性とをマッチさせる
#                 dp[i][j] %= MOD

dp = [0] * (1<<N)
dp[0] = 1
for j in range(0,1<<N):
    i = bin(j).count("1")
    for k in range(0,N):
        if (j>>k)&1 == 1 and a[i-1][k] == 1:
            dp[j] += dp[j^(1<<k)]
            dp[j] %= MOD

ans = dp[(1<<N)-1]
print(ans)

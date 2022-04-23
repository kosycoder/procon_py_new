def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

MOD = 998244353

n, m, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(k):
        for kk in range(1,m+1):
            if j + kk <= k:
                dp[i+1][j+kk] += dp[i][j]
                dp[i+1][j+kk] %= MOD

ans = 0
for i in range(1,k+1):
    ans += dp[n][i]
    ans %= MOD
    i += 1

print(ans)

MOD = 998244353
n = int(input())

dp = []
for _ in range(n+1):
    dp.append([None]*9)

for j in range(9):
    dp[1][j] = 1

for i in range(2,n+1):
    for j in range(9):
        if j == 1 - 1:
            dp[i][j] = (dp[i-1][1-1] + dp[i-1][2-1]) % MOD
        elif j == 9 - 1:
            dp[i][j] = (dp[i-1][8-1] + dp[i-1][9-1]) % MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % MOD

ans = 0
for i in range(9):
    ans += dp[n][i]
    ans %= MOD

print(ans)

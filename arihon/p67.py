n = int(input())
m = int(input())
a = list(map(int,input().split()))
M = int(input())

dp = []
for i in range(n+1):
    dp.append([0] * (m+1))
for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(1,m+1):
        if j-i-a[i]>=0:
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j-1-a[i]] + M) % M
        else:
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M
print(dp[n][m])

n = int(input())
m = int(input())
s = input()
t = input()

s = str(s)
t = str(t)

dp = []
for i in range(n+1):
    dp.append([0]*(m+1))

for i in range(0,n):
    for j in range(0,m):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i][j+1], dp[i+1][j])
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[n][m])

n = int(input())
uv = []
for i in range(n):
    u, v = map(int, input().split())
    uv.append([u,v])
w = int(input())

dp = []
for i in range(n+1):
    dp.append([0]*(w+1))

for i in range(n):
    for j in range(0,w+1):
        if j - uv[i][0] >= 0:
            dp[i+1][j] = max(dp[i][j], dp[i][j-uv[i][0]]+uv[i][1])
        else:
            dp[i+1][j] = dp[i][j]
print(dp)
print(dp[n][w])

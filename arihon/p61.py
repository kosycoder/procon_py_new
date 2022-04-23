INF = int(1e9)

n = int(input())
uv = []
for i in range(n):
    u, v = map(int, input().split())
    uv.append([u,v])
w = int(input())

dp = []
for i in range(n+1):
    dp.append([0]*(101))
for i in range(1,101):
    dp[0][i] = INF

for i in range(n):
    for j in range(0,101):
        if j - uv[i][1] >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i][j-uv[i][1]]+uv[i][0])
        else:
            dp[i+1][j] = dp[i][j]
# print(dp)
# print(dp[n][w])
ans = 0
for j in range(101):
    if dp[n][j]<=w:
        ans = j
print(ans)

# 4
# 2 3
# 1 2
# 3 4
# 2 2

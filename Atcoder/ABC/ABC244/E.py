n, m, k, s, t, x = map(int, input().split())
uv = []
for _ in range(m):
    u, v = map(int, input().split())
    uv.append([u, v])

# dp[k+1][n+1][2]
dp = []
dp0 = [0] * (k+1)
dp0 = [dp0] * (n+1)
dp = [dp0] * 2

for j in range(n+1):
    if j == s:
        dp[0][j][0] = 1
    else:
        dp[0][j][0] = 0
    
    dp[0][j][1] = 0

for i in range(n+m):
    for j in range(k):
        if j == s:
            dp[0][j][0] = 1
        else:
            dp[0][j][0] = 0

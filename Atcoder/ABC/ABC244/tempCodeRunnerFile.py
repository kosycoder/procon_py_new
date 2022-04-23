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

print(dp)

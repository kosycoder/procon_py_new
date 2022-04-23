n = int(input())
a = list(map(int,input().split()))

dp = [0] * n
ans = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)
    ans = max(ans, dp[i])
print(ans)

# 5
# 4 2 3 1 5

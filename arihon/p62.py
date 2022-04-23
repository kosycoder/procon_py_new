n = int(input())
a = list(map(int,input().split()))
m = list(map(int,input().split()))
k = int(input())

dp = [-1] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(k+1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j-a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j-a[i]] - 1

if dp[k] >= 0:
    print("Yes")
else:
    print("No")

# 3
# 3 5 8
# 3 2 2
# 17

INT_MAX = int(2e9)
p = int(input())
q = int(input())
atmp = list(input().split())
atmp = [int(i) for i in atmp]

dp = []
for _ in range(q+1):
    dp.append([None] * (q+2))

def solve():
    a = [None] * (q+2)
    a[0] = 0
    a[q+1] = p + 1
    for i in range(q):
        a[i+1] = atmp[i]
    
    for iq in range(q+1):
        dp[iq][iq+1] = 0
    
    w = 2
    while w <= q + 1:
        i = 0
        while i + w <= q + 1:
            t = INT_MAX

            k = i + 1
            while k < i + w:
                t = min(t, dp[i][k] + dp[k][i+w])
                k += 1

            dp[i][i+w] = t + a[i+w] - a[i] - 2
            i += 1
        w += 1
    
    print(dp[0][q+1])

solve()

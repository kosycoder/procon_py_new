n = int(input())
r = int(input())
x = sorted(list(map(int, input().split())))
print(x)
i, ans = 0, 0
while i < n:
    s = x[i]
    while i < n and x[i] <= s+r: i += 1
    p = x[i-1]
    while i < n and x[i] <= p+r: i += 1
    ans += 1
    
print(ans)

# 6
# 10
# 1 7 15 20 30 50

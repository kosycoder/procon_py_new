n = int(input())
v1 = list(input().split())
v1 = [int(i) for i in v1]
v2 = list(input().split())
v2 = [int(i) for i in v2]
v1.sort()
v2.sort()
v2.reverse()
ans = 0
for i in range(n):
    ans += v1[i] * v2[i]

print(ans)

# 3
# 1 3 -5
# -2 4 1

# 5
# 1 2 3 4 5
# 1 0 1 0 1
def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n = int(input())
m = int(input())
M = 998244353
color = [[False]*m for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == "x":
            color[i][j] = True
        else:
            color[i][j] = False
print(color)

dp = [[0]*(1<<m) for i in range(2)]
def solve():
    crt = dp[0]
    next = dp[1]
    crt[0] = 1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            for used in range(1<<m):
                if ((used >> j) & 1) or color[i][j]:
                    next[used] = crt[used & ~ (1<<j)]
                else:
                    res = 0
                    if ((j + 1 < m) and (not((used >> (j+1) & 1))) and (not(color[i][j+1]))):
                        res += crt[used or 1<<(j+1)]
                    if i + 1 < n and not(color[i+1][j]):
                        res += crt[used or 1<<j]
                    next[used] = res % M
        crt, next = next, crt
    print(crt[0])

solve()

# 3
# 3
# ...
# .x.
# ...
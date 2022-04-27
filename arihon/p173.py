from bisect import bisect, bisect_left, bisect_right


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
INF = int(1e18)
n, e = map(int, input().split())

M = [[INF] * n for _ in range(n)]
for i in range(e):
    x, y, w = list(map(int, input().split()))
    M[x][y] = w

dp = [[INF] * n for _ in range(1<<n)]
dp[(1<<n)-1][0] = 0 #1:訪問済み、、、全部訪問して、今いるところが0ならパスの重みは0

def solve():
    for S in range((1<<n)-2,-1,-1):
        for u in range(n):
            for v in range(n):
                if (not((S >> u)&1)): # uが未訪問ならば
                    dp[S][v] = min(dp[S][v], dp[S|(1<<u)][u] + M[u][v])
    print(dp[0][0])

solve()

# 5 8
# 0 1 3
# 2 0 4
# 0 3 4
# 4 0 7
# 1 2 5
# 4 1 6
# 2 3 5
# 3 4 3


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

n = int(input())
m = int(input())
a = int(input())
b = int(input())
t = list(map(int,input().split()))
c = int(input())

M = [[-1] * m for _ in range(m)]
for i in range(c):
    x, y, w = list(map(int, input().split()))
    x -= 1
    y -= 1
    M[x][y] = w
    M[y][x] = w

dp = [[INF] * m for _ in range(1<<n)]

def solve():

# 2
# 4
# 2
# 1
# 3 1
# 4
# 1 3 3
# 1 4 2
# 2 3 3
# 2 4 5

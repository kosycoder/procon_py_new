dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]

m = int(input())
n = int(input())

tile = []
opt = []
flip = []
for _ in range(m):
    tile1 = input().split()
    tile1 = [int(i) for i in tile1]
    tile.append(tile1)

def get(x, y):
    c = tile[x][y]
    for d in range(5):
        x2, y2 = x + dx[d], y + dy[d]
        if 0 <= x2 < m and 0 <= y2 < n:
            c += flip[x2][y2]
    return c % 2

def calc():
    i = 1
    while i < m:
        j = 0
        while j < n:
            if get(i-1,j):
                flip[i][j] = 1
            j += 1
        i += 1
    
    j = 0
    while j < n:
        if get(m-1,j) != 0:
            return -1
        j += 1
    
    res = 0
    i = 0
    while i < m:
        j = 0
        while j < n:
            res += flip[i][j]
            j += 1
        i += 1
    return res

res = -1
opt = [[None]*n for _ in range(m)]
for i in range(1<<n):
    flip = [[0]*n for _ in range(m)]
    for j in range(n):
        flip[0][n-j-1] = i >> j & 1
    num = calc()
    if (num >= 0 and (res < 0 or res > num)):
        res = num
        for idxm in range(m):
            for idxn in range(n):
                opt[idxm][idxn] = flip[idxm][idxn]

if res < 0:
    print("IMPOSSIBLE")
else:
    print(opt)

# 4
# 4
# 1 0 0 1
# 0 1 1 0
# 0 1 1 0 
# 1 0 0 1

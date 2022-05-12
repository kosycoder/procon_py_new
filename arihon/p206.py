from collections import deque

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

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

X = int(input())
Y = int(input())

field = []
for _ in range(Y):
    g = input()
    field.append(g)

dist = [[-1]*Y for _ in range(X)]
dX = []
dY = []
pX = []
pY = []

def judge(t):
    d = len(dX)
    p = len(pX)

    V = t * d + p
    G = []
    for _ in range(Y):
        g = input()
        G.append(g)
    
    for i in range(d):
        for j in range(p):
            if dist[dX[i]][dY[i]][pX[j]][pY[j]] >= 0:
                for k in range(dist[dX[i]][dY[i]][pX[j]][pY[j]],t+1):
                    add_edge((k-1)*d+i, t*d+j)

    return bipartite_matching() == p

match = [-1] * V
used = [0] * V

def add_edge(u, v):
    G[u].append(v)
    G[v].append(u)

def dfs(v):
    used[v] = True
    for i in range(len(G[v])):
        u = G[v][i]
        w = match[u]
        if w < 0 or not(used[w]) and dfs(w):
            match[u] = v
            match[v] = u
            return True
    return False

def bipartite_matching():
    res = 0
    for v in range(V):
        if match[v] < 0:
            used = [0] * n
            if dfs(v):
                res += 1
    
    return res

def bfs(x, y):
    d = [[-1]*Y for _ in range(X)]
    qx = deque()
    qy = deque()
    d[x][y] = 0
    qx.append(x)
    qy.append(y)

    while len(qx):
        x = qx.popleft()
        y = qy.popleft()
        for k in range(4):
            x2 = x + dx[k]
            y2 = y + dy[k]
            if 0<=x2 and x2<X and 0<=y2 and y2<Y and field[x2][y2]=="." and d[x2][y2]<0:
                d[x2][y2] = d[x][y] + 1
                qx.append(x2)
                qy.append(y2)

def solve():
    n = X * Y
    for x in range(X):
        for y in range(Y):
            if field[x][y] == "D":
                dX.append(x)
                dY.append(y)
                bfs(x, y, dist[x][y])
            elif field[x][y] == ".":
                pX.append(x)
                pY.append(y)



# 5
# 5
# XXDXX
# X...X
# D...X
# X...D
# XXXXX



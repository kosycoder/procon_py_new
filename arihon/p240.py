def DEBUG(debugoutput, flg = False):
    if flg:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
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

dx, dy = [-1, -1, 1, 1], [-1, 0, -1, 0]

DEBUGFLG = False

M = int(input())
N = int(input())
V = M * N

seat = []
for _ in range(M):
    seat.append(input())
DEBUG(seat, DEBUGFLG)

G = [[] for _ in range(V)]
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
            used = [0] * N
            if dfs(v):
                res += 1
    
    return res

def solve():
    num = 0
    for y in range(M):
        for x in range(N):
            if seat[y][x] == ".":
                num += 1
                for k in range(4):
                    x2 = x + dx[k]
                    y2 = y + dy[k]
                    if 0 <= x2 < N and 0 <= y2 < M and seat[y2][x2] == ".":
                        add_edge(x * M + y, x2 * M + y2)
    
    print(num - bipartite_matching())

solve()

# 2
# 3
# ...
# ...

# 2
# 3
# x.x
# xxx

# 2
# 3
# x.x
# x.x
# 2

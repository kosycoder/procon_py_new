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

# dx, dy = [-1, -1, 1, 1], [-1, 0, -1, 0]

DEBUGFLG = False

N, K = map(int,input().split())
price = []
for _ in range(N):
    p1, p2 = map(int,input().split())
    price.append([p1, p2])

V = 2 * N
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
    for i in range(N):
        for j in range(N):
            if i == j: 
                continue
            flg = True
            for k in range(K):
                if price[j][k] >= price[i][k]:
                    flg = False
            if flg:
                add_edge(i, N + j)
    
    print(N - bipartite_matching())

solve()

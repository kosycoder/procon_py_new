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
k = int(input())
V = 2 * n
rc = [input_intarray() for _ in range(k)]
match = [-1] * V
used = [0] * V

G = [[] for _ in range(V)]
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

def solve():
    for i in range(k):
        add_edge(rc[i][0]-1, n+rc[i][1]-1)
    print(bipartite_matching())

solve()

# 3
# 4
# 1 1
# 1 3
# 2 2
# 3 2

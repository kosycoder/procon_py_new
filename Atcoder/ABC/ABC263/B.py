from collections import deque

def DEBUG(debugoutput):
    if DEBUGFLG:
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

def make_graph_noweight():
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        graph[P[i]].append(i+1)
    return graph

def bfs(s):
    d = [None] * N # uからの距離の初期化
    p = [None] * N # 親ノードの初期化
    d[s] = 0 # 開始点と開始点との距離は0
    p[s] = -1 # 開始点自身が親
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if d[v] is None:
                d[v] = d[u] + 1
                p[v] = u
                queue.append(v)
    return d, p

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N = int(input())
P = input().split()
P = [int(int(i)-1) for i in P]
g = make_graph_noweight()
d, p = bfs(0)
print(d[N-1])

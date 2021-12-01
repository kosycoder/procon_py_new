import sys
input = sys.stdin.readline

def make_graph_noweight():
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # 有向グラフなら消す
    return graph  # [[1, 2, 4], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [0, 2, 3]]


from collections import deque

def isbipartite(s):
    d = [None] * n # uからの距離の初期化
    p = [None] * n # 親ノードの初期化
    d[s] = 0 # 開始点と開始点との距離は0
    p[s] = -1 # 開始点自身が親
    c = [None] * n
    for itrn in range(n):
        c[itrn] = int(input())
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if d[v] is None:
                d[v] = d[u] + 1
                p[v] = u
                queue.append(v)
                if c[u] == c[v]:
                    return False
    return True

# 0からの各頂点の距離
n, m = map(int, input().split())
g = make_graph_noweight()
print(isbipartite(0))

# 11 9
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# 2 6
# 3 7
# 5 8
# 8 9
# 0
# 1
# 1
# 0
# 0
# 0
# 0
# 1
# 1
# 0
# 0
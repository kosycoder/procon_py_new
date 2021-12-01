import heapq
INF = 10 ** 9
V, E, S = map(int, input().split()) # 頂点、辺、開始点
# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
dist = [[float("inf") for i in range(V)] for i in range(V)]
# ②自分自身へのコストは０
for i in range(V):
    dist[i][i] = 0
for e in range(E):
    s, t, w = map(int, input().split())
    dist[s][t] = w
    dist[t][s] = w

# dist[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k]!=INF and dist[k][j]!=INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
print(dist)

# 4 6 0
# 0 1 2
# 1 2 1
# 2 3 1
# 3 0 1
# 0 2 3
# 1 3 5

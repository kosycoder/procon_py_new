# from collections import deque
# from operator import truediv

# INF = int(1e9)

# n = int(input())
# r = int(input())
# G = []
# for i in range(n):
#     G.append([INF]*n)
# for i in range(r):
#     a, b, c= map(int, input().split())
#     a -= 1
#     b -= 1
#     G[a][b] = c
#     G[b][a] = c

# used = [False] * n
# d1 = [INF] * n
# d2 = [INF] * n

# def dijkstra(u0):
#     d1[u0] = 0
#     d2[u0] = 0
#     while(1):
#         v = -1
#         for u in range(v):
#             if used[u] == 0 and (v == -1 or d1[u] < d1[v]):
#                 v = u
#             if v == -1:
#                 break
#             used[v] = True
#         for u in range(v):
#             if d1[u] > d1[v] + G[v][u]:
#                 d2[u] = d1[u]
#                 d1[u] = d1[v] + G[v][u]

# dijkstra(0)
# print(d1[n-1])
# print(d2[n-1])

from collections import deque
from operator import truediv
import heapq

INF = int(1e9)

n = int(input())
r = int(input())
G = [[] for _ in range(n)]
for _ in range(r):
    a, b, c= map(int, input().split())
    a -= 1
    b -= 1
    G[a].append([b, c])
    G[b].append([a, c])

used = [False] * n
dist1 = [INF] * n
dist2 = [INF] * n

def dijkstra(u0):
    Q = list()
    heapq.heapify(Q)
    dist1[0] = 0
    Q.append([0, 0])

    while(len(Q)!=0):
        d, v = Q.pop()
        ## 今見ている辺が3番目以降に最短
        if dist2[v] < d:
            continue
        for w, cost in G[v]:
            d2 = d + cost
            ## 今見ている辺が最短経路
            if dist1[w] > d2:
                dist1[w], d2 = d2, dist1[w]
                Q.append([dist1[w], w])
            ## 今見ている辺が次点の最短経路
            if dist2[w] > d2 and dist1[w] < d2:
                dist2[w] = d2
                Q.append([dist2[w], w])
dijkstra(0)
print(dist1)
print(dist2)

# 4
# 4
# 1 2 100
# 2 4 200
# 2 3 250
# 3 4 100
def make_graph_noweight():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)  # 有向グラフなら消す
    print(graph)  # [[1, 2, 4], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [0, 2, 3]]

def make_graph_weight():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n):
        u, v, w = map(int, input().split())
        graph[u-1].append([v-1, w])
        graph[v-1].append([u-1, w])  # 有向グラフなら消す
    print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]

make_graph_noweight()


5 8
1 2
1 3
1 5
2 3
2 4
3 4
3 5
4 5
import heapq
INF = 10 ** 9
V, E, S = map(int, input().split()) # 頂点、辺、開始点
adj = [ [] for v in range(V)] # 隣接リスト
for e in range(E):
    s, t, w = map(int, input().split())
    adj[s].append((t,w))
    adj[t].append((s,w))

dist = [INF] * V
visited = [False] * V # 訪問フラグ
pq = [] # 優先度付きキュー
dist[S] = 0
heapq.heappush(pq, (0, S))

# visited[S] = True # 始点の訪問フラグを立てる

# ans = 0
# now_s = S
while(pq):
    w, t = heapq.heappop(pq)
    if visited[t]: # 訪問済みならスキップ
        continue
    visited[t] = True # 訪問フラグを立てる
    # ans += w # スコアに加算
    # print(now_s,end=" ")
    # print(t)
    # now_s = t
    for s, w in adj[t]: # 隣接する頂点を列挙
        if visited[s] == False and (dist[t] + w < dist[s]): # 未訪問なら探索候補としてpqに追加
            dist[s] = dist[t] + w
            heapq.heappush(pq, (dist[s], s))
print(dist)

# 4 6 0
# 0 1 2
# 1 2 1
# 2 3 1
# 3 0 1
# 0 2 3
# 1 3 5

#トポロジカルソート、DAG Directed Acyclic Graph

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())


edges = []
for i in range(N):
    edges.append([])

# 始点の判定につかう入次数
indeg = [0]*N

for i in range(M):
    x, y = list(map(int, input().split()))
    edges[x-1].append(y-1)
    indeg[y-1] += 1

# 閉路のない有効グラフにはトポロジカルソートが存在する。
# length[i]: iを始点とするパスのうち、最も長いものの長さを管理。
length = [0] * N
done = [False] * N

def rec(i):
    #計算すみであれば値を返す
    if done[i]:
        return length[i]
    # そうでなければ値を計算する
    length[i] = 0
    for j in edges[i]:
        length[i] = max(length[i], rec(j)+1)
    
    done[i] = True
    return length[i]

# 視点全てについてrecを呼び出す
for i in range(N):
    if indeg[i] == 0:
        rec(i)

# 答えはlengthの最大値
print(max(length))
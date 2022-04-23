from collections import deque

v = int(input())
e = int(input())
G = []
for i in range(v):
    G.append([False]*v)
for i in range(e):
    a, b= map(int, input().split())
    G[a][b] = True
    G[b][a] = True

visit = [-1] * v
parent = [-1] * v
color = [-1] * v
dq = deque()

def bfs(u0):
    visit[u0] = 0
    color[u0] = 0
    dq.append(u0)
    while(len(dq)!=0):
        u = dq.popleft()
        visit[u] = 0
        for i in range(v):
            if G[u][i] == False:
                continue
            else:
                if color[u] == color[i]:
                    return False
                if visit[i] == -1:
                    dq.append(i)
                    visit[i] = 0
                    if color[u] == 0:
                        color[i] = 1
                    else:
                        color[i] = 0
        visit[u] = 1
    return True

if bfs(0):
    print("Yes")
else:
    print("No")

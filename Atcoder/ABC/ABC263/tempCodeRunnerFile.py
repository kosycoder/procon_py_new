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

def bfs(s):
    d = [None] * N
    p = [None] * N
    d[s] = 0
    p[s] = -1
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
g = [[] for _ in range(N)]
for i in range(N-1):
    g[P[i]].append(i+1)

d, p = bfs(0)

print(d[N-1])

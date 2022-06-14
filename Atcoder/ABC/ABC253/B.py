from collections import deque

def DEBUG(debugoutput, flg = False):
    if flg:
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

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

H, W = map(int,input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)
search = 1
for h in range(H):
    for w in range(W):
        if search == 1:
            if S[h][w] == "o":
                h_start = h
                w_start = w
                search += 1
        if search == 2:
            if S[h][w] == "o":
                h_end = h
                w_end = w
                break

DEBUG(S, DEBUGFLG)
DEBUG([h_start, w_start, h_end, w_end], DEBUGFLG)

def bfs(h, w):
    d = [[None] * W for _ in range(H)]
    d[h][w] = 0
    queueh = deque()
    queuew = deque()
    queueh.append(h)
    queuew.append(w)
    while queueh:
        uh = queueh.popleft()
        uw = queuew.popleft()
        for v in range(4):
            if 0<=uh+dy[v]<=H-1 and 0<=uw+dx[v]<=W-1:
                h2 = uh + dy[v]
                w2 = uw + dx[v]
                DEBUG(h2, DEBUGFLG)
                DEBUG(w2, DEBUGFLG)
                if d[h2][w2] == None:
                    DEBUG(d[h2][w2], DEBUGFLG)
                    d[h2][w2] = d[uh][uw] + 1
                    queueh.append(h2)
                    queuew.append(w2)
    return d

d = bfs(h_start, w_start)
print(d[h_end][w_end])

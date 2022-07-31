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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N, M = map(int,input().split())
G = [[0]*N for _ in range(N)]
for i in range(M):
    U, V = map(int,input().split())
    U -= 1
    V -= 1
    G[U][V] = 1
    G[V][U] = 1

ans = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            if G[a][b] == 1 and G[b][c] == 1 and G[c][a] == 1:
                if a < b < c:
                    ans += 1

print(ans)

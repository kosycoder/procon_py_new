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

def calcdistance(x1, y1, x2, y2):
    return pow((x1-x2)**2 + (y1-y2)**2, 0.5)

N, K = map(int,input().split())
A = input_intarray()
A = [int(i-1) for i in A]
X = []
Y = []
for i in range(N):
    Xtmp, Ytmp = map(int,input().split())
    X.append(Xtmp)
    Y.append(Ytmp)

havelamp = [False] * N
for valA in A:
    havelamp[valA] = True
DEBUG(havelamp)

ans = 0
for valN in range(N):
    if havelamp[valN]:
        continue
    
    anstmp = 1e18
    for valA in A:
        anstmp = min(anstmp, calcdistance(X[valN], Y[valN], X[valA], Y[valA]))
    ans = max(ans, anstmp)

print(ans)

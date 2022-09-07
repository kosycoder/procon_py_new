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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# MOD = 998244353

DEBUGFLG = False

N, M, T = map(int,input().split())
A = input().split()
A = [int(i) for i in A]
XY = []
for _ in range(M):
    Xtmp, Ytmp = map(int,input().split())
    XY.append([Xtmp-1, Ytmp])

def solve():
    t = T
    j = 0
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if j<M:
            if i+1 == XY[j][0]:
                t += XY[j][1]
                j += 1
    print("Yes")
    DEBUG(t)

solve()


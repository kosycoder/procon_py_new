from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

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

DEBUGFLG = True
MOD = 10**9+7
BLACK = 0
WHITE = 1

N = int(input())
xy = [[] for _ in range(N+1)]
for _ in range(N-1):
    xtmp, ytmp = map(int,input().split())
    xy[xtmp].append(ytmp)
    xy[ytmp].append(xtmp)

dpwhite = [0] * (N+1)
dpblack = [0] * (N+1)
flg = [False] * (N+1)
def memodp(i):
    if flg[i]:
        return

    flg[i] = True
    dpblack[i] = 1
    dpwhite[i] = 1
    for valy in xy[i]:
        if flg[valy]:
            continue
        memodp(valy)
        dpwhite[i]*=(dpwhite[valy]+dpblack[valy])
        dpwhite[i]%=MOD
        dpblack[i]*=dpwhite[valy]
        dpblack[i]%=MOD

memodp(1)
print((dpwhite[1]+dpblack[1])%MOD)

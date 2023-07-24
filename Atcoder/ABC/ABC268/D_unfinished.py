from collections import defaultdict
import itertools

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

DEBUGFLG = True

N, M = map(int,input().split())
S = []
for _ in range(N):
    Sin = input()
    S.append(Sin)

T = defaultdict()
for _ in range(M):
    Tin = input()
    T[Tin] = 1

xarr = []
for i in range(N):
    xarr.append(str(i))
print(xarr)

for x in itertools.permutations(xarr):
    word = str()
    cnt = 0
    for valx in xarr:
        if cnt == 0:
            word = word + str(S[int(valx)])
            cnt += 1
        else:
            word = word + str(_)*(1+underbar[cnt]) + str(S[int(valx)])
        DEBUG(word)
        if len(word)>16:
            continue

    if word in T or len(word)>16:
        continue
    else:
        print(word)
        exit()

print(-1)

from collections import defaultdict

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

N = int(input())
pe = [[] for _ in range(N)]
dicLCM = defaultdict(int)
for valN in range(N):
    mi = int(input())
    for _ in range(mi):
        pii, eii = map(int,input().split())
        pe[valN].append([pii, eii])
        if dicLCM[pii] < eii:
            dicLCM[pii] = eii

cnt = defaultdict(int)
for valN in range(N):
    for valpe in pe[valN]:
        valp = valpe[0]
        vale = valpe[1]
        if dicLCM[valp] == vale:
            cnt[valp] += 1

ans = 0
for valN in range(N):
    flg = False
    for valpe in pe[valN]:
        valp = valpe[0]
        vale = valpe[1]
        DEBUG(valpe)
        if (dicLCM[valp] == vale and cnt[valp] == 1):
            flg = True
            break
    DEBUG("----")
    if flg:
        ans += 1

print(min(ans + 1, N))

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
MOD = int(1e9+7)

H, W = map(int,input().split())
a = []  #0-idx
for valW in range(H):
    atmp = input()
    a.append(atmp)

dp = [[0] * (W+1) for _ in range(H+1)]
for valH in range(1,H+1):
    for valW in range(1,W+1):
        if valW == 1 and valH == 1:
            dp[valH][valW] = 1
            continue
        if a[valH-1][valW-1] ==".":
            dp[valH][valW] = dp[valH-1][valW] + dp[valH][valW-1]
            dp[valH][valW] %= MOD
        else:
            dp[valH][valW] = 0

DEBUG(dp)
print(dp[H][W])

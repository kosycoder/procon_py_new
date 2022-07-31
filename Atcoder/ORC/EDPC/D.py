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

N, W = map(int,input().split())
w = [0]
v = [0]
for _ in range(N):
    win, vin = map(int,input().split())
    w.append(win)
    v.append(vin)

dp = [[0] * (W+1) for _ in range(N+1)]
for valN1 in range(1,N+1):
    wnow = w[valN1]
    vnow = v[valN1]
    for valW in range(1, W+1):
        if valW - wnow >=0:
            dp[valN1][valW] = max(dp[valN1-1][valW], dp[valN1-1][valW-wnow] + vnow)
        else:
            dp[valN1][valW] = dp[valN1-1][valW]

DEBUG(dp)
print(max(dp[N]))

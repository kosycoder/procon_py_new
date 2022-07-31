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
maxV = sum(v)

dp = [[int(1e18)] * (maxV+1) for _ in range(N+1)]
dp[0][0] = 0
for valN1 in range(1,N+1):
    wnow = w[valN1]
    vnow = v[valN1]
    # dp[valN1][v[valN1]] = w[valN1]
    for valV in range(0,maxV+1):
        if valV - vnow >= 0:
            dp[valN1][valV] = min(dp[valN1-1][valV], dp[valN1-1][valV-vnow] + wnow)
        else:
            dp[valN1][valV] = dp[valN1-1][valV]
for i in range(N+1):
    DEBUG(dp[i])
ans = -1
for i in range(1,maxV+1):
    if dp[N][i]<= W:
        ans = i
print(max(ans,0))

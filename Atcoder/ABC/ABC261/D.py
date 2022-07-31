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
INF = int(1e18)

N, M = map(int,input().split())
Xin = input_intarray()
X = [0]
for valx in Xin:
    X.append(valx)
Y = [0]*(N+1)
for i in range(M):
    Cin, Yin = map(int,input().split())
    Y[Cin] = Yin

dp = [[-INF]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for itimes in range(1,N+1):
    for jcount in range(0,itimes+1):
        if jcount == 0:
            for j in range(itimes):
                dp[itimes][jcount] = max(dp[itimes][jcount], dp[itimes-1][j])
        else:
            dp[itimes][jcount] = dp[itimes-1][jcount-1] + X[itimes] + Y[jcount]

print(max(dp[N]))

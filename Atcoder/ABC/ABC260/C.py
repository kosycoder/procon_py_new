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

N, X, Y = map(int,input().split())

dp = [0 for i in range(N+1)]
ep = [0 for i in range(N+1)]
dp[1] = 0
ep[1] = 1

for n in range(2,N+1):
    ep[n] = dp[n-1] + ep[n-1] * Y
    dp[n] = dp[n-1] + ep[n] * X

print(dp[N])

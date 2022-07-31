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

N, K = map(int,input().split())
htmp = input().split()
htmp = [int(i) for i in htmp]
h = [0]
for valhtmp in htmp:
    h.append(valhtmp)

dp = [int(1e18)] * (N+1)
dp[1] = 0
dp[2] = abs(h[1]-h[2])
for num in range(3,N+1):
    dpnumtmp = int(1e18)
    for k in range(1,K+1):
        dpnumtmp = min(dpnumtmp, dp[num-k]+abs(h[num]-h[num-k]))
        if num-k == 0:
            break
    dp[num] = dpnumtmp

DEBUG(dp)
print(dp[N])

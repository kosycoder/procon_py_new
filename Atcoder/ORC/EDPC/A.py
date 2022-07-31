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
h = input().split()
h = [int(i) for i in h]

dp = [0] * (N+1)
dp[1] = 0
dp[2] = abs(h[0]-h[1])
for num in range(3,N+1):
    dp[num] = min(dp[num-1]+abs(h[num-1]-h[num-2]), dp[num-2]+abs(h[num-3]-h[num-1]))
DEBUG(dp)
print(dp[N])

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
ptmp = input().split()
ptmp = [float(valp) for valp in ptmp]
p = [0]
for valptmp in ptmp:
    p.append(valptmp)

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(0,N+1):
    dp[i][0] = 1.0

for valN1 in range(1,N+1):
    for valN2 in range(1,valN1+1):
        dp[valN1][valN2] = dp[valN1-1][valN2]*(1-p[valN1]) + dp[valN1-1][valN2-1]*p[valN1]

print(dp[N][N//2+1])

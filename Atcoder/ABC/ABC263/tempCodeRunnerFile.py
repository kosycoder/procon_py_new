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
MOD = 998244353

N = int(input())
Atmp = input().split()
Atmp = [int(i) for i in Atmp]
A = [0, *Atmp]
dp = [0] * (N+1)
dpS = [0]
for i in range(N):
    dpS.append((dpS[i]*pow(A[N-i-1],MOD-2,MOD))%MOD)
    dpS[i+1] += (A[N-i-1]+1)*pow(A[N-i-1],MOD-2,MOD)%MOD
    dpS[i+1] %= MOD
dpS.reverse()

for i in range(N-1,0,-1):
    dp[i] = dpS[i+1] - dpS[i-A[i]+1]
    # dp[i] += (A[i]+1)*pow(A[i],MOD-2,MOD)%MOD
    # dp[i] %= MOD

DEBUG(dp)
print(dp[1])

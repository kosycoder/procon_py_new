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

N = int(input())
a = input().split()
a = [int(i) for i in a]
c = [0, 0, 0, 0]
for i in range(N):
    c[a[i]] += 1
DEBUG(c)

dp = [[[0.0] * (N+2) for _ in range(N+2)] for _ in range(N+2)]
for k in range(0,N+1):
    for j in range(0,N+1):
        for i in range(0,N+1):
            if i == j == k == 0:
                continue
            else:
                dptmp = 1.0
                if i:
                    dptmp += dp[i-1][j][k]*i/N
                if j:
                    dptmp += dp[i+1][j-1][k]*j/N
                if k:
                    dptmp += dp[i][j+1][k-1]*k/N
                dptmp *= N/(i+j+k)
                dp[i][j][k] = dptmp
            if i+j+k>N:
                break

DEBUG(dp)
print(dp[c[1]][c[2]][c[3]])

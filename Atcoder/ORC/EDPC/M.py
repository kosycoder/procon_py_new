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

N, K = map(int,input().split())
a = [-1]
atmp = input().split()
atmp = [int(i) for i in atmp]
for valatmp in atmp:
    a.append(valatmp)

# dp[i][j] = i番目の子供までにj個渡す
dp = [[0] * (K+1) for _ in range(N+1)]
dpsum_im1 = [0] * (K+2)
dp[0][0] = 1
for i in range(1,N+1):
    dpsum_im1[0] = 0
    for j in range(1,(K+1)+1):
        dpsum_im1[j] = dpsum_im1[j-1] + dp[i-1][j-1]
        dpsum_im1[j] %= MOD
    for j in range(0,K+1):
        dp[i][j] = dpsum_im1[j+1] - dpsum_im1[max(0,j-a[i])] + MOD
        dp[i][j] %= MOD
                
print(dp[N][K])
DEBUG(dp)
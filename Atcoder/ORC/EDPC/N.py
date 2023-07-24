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
a = input().split()
a = [int(i) for i in a]
S = [0]
for i in range(N):
    S.append(S[i]+a[i])

INF = 1e18

dp = [[0]*N for _ in range(N)]
flg = [[False]*N for _ in range(N)]
def solve(l,r):
    if flg[l][r]:
        return dp[l][r]
    flg[l][r] = True
    
    if l == r:
        return 0
    
    ans  = INF
    for m in range(l,r):
        ans = min(ans, solve(l,m)+solve(m+1,r))
    dp[l][r] = ans + S[r+1] - S[l-1+1]
    return dp[l][r]

ans = solve(0,N-1)
print(ans)

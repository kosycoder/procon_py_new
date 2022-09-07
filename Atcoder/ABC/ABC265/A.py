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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# MOD = 998244353

DEBUGFLG = False
X, Y, N = map(int,input().split())

if N % 3 == 0:
    ans = min(N//3*Y, X*N)
elif N % 3 == 1:
    ans = min(N//3*Y+X, X*N)
else:
    ans = min(N//3*Y+2*X, X*N)
print(ans)
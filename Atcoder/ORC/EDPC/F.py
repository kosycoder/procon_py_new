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

s = input()
t = input()
n = len(s)
m = len(t)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
nowlength = dp[n][m]
nown = n
nowm = m
while nowlength > 0:
    if s[nown-1] == t[nowm-1]:
        ans += s[nown-1]
        nown -= 1
        nowm -= 1
        nowlength -= 1
    elif dp[nown][nowm] == dp[nown-1][nowm]:
        nown -= 1
    else:
        nowm -= 1

print(ans[::-1])

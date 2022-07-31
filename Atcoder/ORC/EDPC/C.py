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
a = [0]
b = [0]
c = [0]
for _ in range(N):
    ain, bin, cin = map(int,input().split())
    a.append(ain)
    b.append(bin)
    c.append(cin)

dp = [[0] * (3) for _ in range(N+1)]
DEBUG(dp)
for num in range(1,N+1):
    DEBUG(num)
    dp[num][0] = max(dp[num-1][1], dp[num-1][2]) + a[num]
    dp[num][1] = max(dp[num-1][0], dp[num-1][2]) + b[num]
    dp[num][2] = max(dp[num-1][0], dp[num-1][1]) + c[num]

DEBUG(dp)
print(max(dp[N][0], dp[N][1], dp[N][2]))

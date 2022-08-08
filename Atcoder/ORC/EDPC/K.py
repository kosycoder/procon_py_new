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
a = input().split()
a = [int(i) for i in a]

dp = [False] * (K+1)
for i in range(1,K+1):
    for j in range(0,N):
        if(i-a[j]>=0 and dp[i-a[j]]==False):
            dp[i] = True

if dp[K]:
    print("First")
else:
    print("Second")


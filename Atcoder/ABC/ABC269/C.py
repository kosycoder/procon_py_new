# from collections import defaultdict

# from sys import setrecursionlimit
# setrecursionlimit(10 ** 6)


def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
    return l

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# MOD = 998244353

DEBUGFLG = False

X = int(input())

s = []
while X > 0:
    if X & 1:
        s.append(1)
    else:
        s.append(0)
    X = X // 2

cnt1 = 0
cnt2 = 0
t = []
for vals in s:
    if vals == 1:
        cnt1 += 1
        t.append(cnt2)
    cnt2 += 1


for i in range(pow(2,cnt1)):
    ans = 0
    cnt = 0
    cnt0 = 0
    for j in range(len(s)):
        if s[j] == 1:
            if ((i>>(t[cnt]-cnt0)) & 1) == 1: 
                ans += int(pow(2,t[cnt]))
            cnt += 1
        else:
            cnt0 += 1
    print(ans)

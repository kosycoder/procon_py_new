# from collections import defaultdict

# from sys import setrecursionlimit
# setrecursionlimit(10 ** 6)

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

a = input().split()
a = [int(i) for i in a]
a = sorted(a)

ans = 1
for i in range(4):
    if a[i] != a[i+1]:
        ans += 1

print(ans)

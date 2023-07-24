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

s = []
for i in range(10):
    s.append(input())
start = True

for i in range(10):
    for j in range(10):
        if s[i][j] == "#":
            if start == True:
                start =  False
                a = i + 1
                c = j + 1
            b = i + 1
            d = j + 1
print(a, b)
print(c, d)


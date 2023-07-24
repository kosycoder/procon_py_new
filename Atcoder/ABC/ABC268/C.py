from re import I


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

DEBUGFLG = True

N = int(input())
p = input().split()
p = [int(i) for i in p]

c = [0] * N

ans = 0
for i in range(N):
    for j in range(-1,2):
        c[(p[i]-i+j+N)%N] += 1

print(max(c))

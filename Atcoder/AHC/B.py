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

D = int(input())
c = input_intarray()
s = []
for _ in range(D):
    si = input_intarray()
    s.append(si)

ans = 0
dlast = [0] * 26
for d in range(D):
    t = int(input()) - 1
    dlast[t] = d + 1
    ans += s[d][t]
    for alphabet in range(26):
        DEBUG(c[alphabet]*(d+1-dlast[alphabet]))
        ans -= c[alphabet]*(d+1-dlast[alphabet])
    print(ans)

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
csum = sum(c)
s = []
for _ in range(D):
    si = input_intarray()
    s.append(si)

tday = []
for _ in range(D):
    tday.append(int(input()))

M = int(input())
dq = []
for _ in range(M):
    di, qi = map(int,input().split())
    dq.append((di, qi))

for m in range(M):
    ans = 0
    dlast = [0] * 26
    tday[dq[m][0]-1] = dq[m][1]
    for d in range(D):
        alphabettoday = tday[d] - 1
        ans += s[d][alphabettoday]
        ans -= c[alphabettoday]*(d+1-dlast[alphabettoday])*(d-dlast[alphabettoday])//2
        dlast[alphabettoday] = d + 1
    for alphabet in range(26):
        ans -= c[alphabet]*(d+2-dlast[alphabet])*(d+1-dlast[alphabet])//2
    print(ans)

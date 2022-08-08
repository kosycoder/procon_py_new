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

N, L, R = map(int,input().split())
a = input().split()
a = [int(i) for i in a]
S = [0]
for i in range(N):
    S.append(S[i]+a[i])

S2 = []
for i in range(N+1):
    if i==0:
        S2.append(S[N-i]-R*(N-i))
    else:
        S2.append(min(S2[i-1], S[N-i]-R*(N-i)))
S2.reverse()

ans = int(1e18)
for x in range(N+1):
    anstmp = R*N + L*x - S[x] + S2[x]
    ans = min(ans, anstmp)
print(ans)

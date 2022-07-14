from itertools import accumulate


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

N, X = map(int,input().split())
A = []
B = []
for _ in range(N):
    Ain, Bin = map(int,input().split())
    A.append(Ain)
    B.append(Bin)

opentime = [A[0]+B[0]]
ans = int(1e19)
for i in range(min(N,X)):
    if i != 0:
        opentime.append(opentime[len(opentime)-1]+A[i]+B[i])
    anstmp = opentime[i] + B[i] * (X-i-1)
    ans = min(ans, anstmp)
    DEBUG(anstmp)

DEBUG(opentime)
print(ans)
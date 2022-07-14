import bisect

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

N, Q = map(int,input().split())
A = input_intarray()
A = sorted(A)
S = [0]
for i in range(len(A)):
    S.append(S[i]+A[i])
DEBUG(S)
for valq in range(Q):
    X = int(input())
    idx = bisect.bisect_right(A, X) - 1
    DEBUG(idx)
    SL = S[idx+1]
    DEBUG(SL)
    SR = S[N] - S[idx+1]
    DEBUG(SR)
    ans = X*(idx+1)-SL + SR-X*(N-(idx+1))
    print(ans)

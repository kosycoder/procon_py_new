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
A = input_intarray()
B = []
C = []
for valA in A:
    B.append(valA)
B = sorted(B)

x = [[] for _ in range(K)]
for i in range(K):
    cnt = 0
    while i+cnt*K < N:
        x[i].append(A[i+cnt*K])
        cnt += 1
    x[i] = sorted(x[i])
DEBUG(x)

idx = 0
for i in range(N):
    C.append(x[i%K][idx])
    if (i+1) % K == 0:
        idx += 1

flg = True
for i in range(N):
    if B[i] != C[i]:
        flg = False
        break

DEBUG(B)
DEBUG(C)
YesNo(flg)

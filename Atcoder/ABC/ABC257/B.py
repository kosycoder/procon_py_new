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

N, K, Q = map(int,input().split())
A = input_intarray()
L = input_intarray()
DEBUG(A)
DEBUG(L)

for valL in L:
    valL -= 1
    DEBUG(valL)
    DEBUG(A[valL])
    if A[valL] == N:
        DEBUG(A)
        continue

    if valL == K - 1:
        A[valL] += 1
    else:
        if A[valL]+1 < A[valL+1]:
            A[valL] += 1
    DEBUG(A)

print(*A)

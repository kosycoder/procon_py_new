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

N, X, Y, Z = map(int,input().split())
A = input_intarray()
B = input_intarray()

ans = []
namelist = [False] * N
PA = [[-1] for _ in range(101)]
for i in range(len(A)):
    PA[A[i]].append(i+1)

cntX = 0
cntall = 0
while cntX < X and cntall < N:
    for i in range(100,-1,-1):
        if len(PA[i]) == 1:
            continue
        for j in range(len(PA[i])):
            if j == 0:
                continue
            if namelist[PA[i][j]-1] == True:
                continue
            namelist[PA[i][j]-1] = True
            ans.append(PA[i][j])
            cntX += 1
            if cntX == X:
                break
        if cntX == X:
            break
    cntall += 1

PB = [[-1] for _ in range(101)]
for i in range(len(B)):
    PB[B[i]].append(i+1)
cntY = 0
cntall = 0
while cntY < Y and cntall < N:
    for i in range(100,-1,-1):
        if len(PB[i]) == 1:
            continue
        for j in range(len(PB[i])):
            if j == 0:
                continue
            if namelist[PB[i][j]-1] == True:
                continue
            namelist[PB[i][j]-1] = True
            ans.append(PB[i][j])
            cntY += 1
            if cntY == Y:
                break
        if cntY == Y:
            break
    cntall += 1

PAplusB = [[-1] for _ in range(201)]
for i in range(len(A)):
    PAplusB[A[i]+B[i]].append(i+1)
cntZ = 0
cntall = 0
while cntZ < Z and cntall < N:
    for i in range(200,-1,-1):
        if len(PAplusB[i]) == 1:
            continue
        for j in range(len(PAplusB[i])):
            if j == 0:
                continue
            if namelist[PAplusB[i][j]-1] == True:
                continue
            namelist[PAplusB[i][j]-1] = True
            ans.append(PAplusB[i][j])
            cntZ += 1
            if cntZ == Z:
                break
        if cntZ == Z:
            break
    cntall += 1

ans = sorted(ans)
for valans in ans:
    print(valans)
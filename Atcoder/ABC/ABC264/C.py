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

DEBUGFLG = False

H1, W1 = map(int,input().split())
A = []
for _ in range(H1):
    Atmp = input().split()
    Atmp = [int(i) for i in Atmp]
    A.append(Atmp)

H2, W2 = map(int,input().split())
B = []
for _ in range(H2):
    Btmp = input().split()
    Btmp = [int(i) for i in Btmp]
    B.append(Btmp)

for i in range(1<<H1):
    for j in range(1<<W1):
        ichecksum = 0
        for ii in range(H1):
            if i & (1 << ii):
                ichecksum += 1

        jchecksum = 0
        for jj in range(W1):
            if j & (1 << jj):
                jchecksum += 1

        if ichecksum != H2 or jchecksum != W2:
            continue
        
        flg = True
        cnt = 0
        for k in range(H1):
            Ctmp = []
            if not(i & (1<<k)):
                continue
            for l in range(W1):
                if not(j & (1<<l)):
                    continue
                Ctmp.append(A[k][l])
            if Ctmp == B[cnt]:
                DEBUG(flg)
                DEBUG(Ctmp)
                cnt += 1
            else:
                flg = False
                break
        if flg and cnt == H2:
            print("Yes")
            exit()
print("No")

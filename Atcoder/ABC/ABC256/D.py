def DEBUG(debugoutput, flg = False):
    if flg:
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

DEBUGFLG = True

N = int(input())
L = []
R = []
for _ in range(N):
    Li, Ri = input_intarray()
    L.append(Li)
    R.append(Ri)

RL = sorted(zip(R,L))
DEBUG(RL, DEBUGFLG)

Rnow = RL[0][0]
Lnow = RL[0][1]
Lans = []
Rans = []
for i in range(N):
    if i == 0:
        if N == 1:
            Lans.append(Lnow)
            Rans.append(Rnow)
            break
        else:
            continue
    
    Rnext = RL[i][0]
    Lnext = RL[i][1]
    if Lnext <= Rnow:
        Rnow = Rnext
        if Lnext <= Lnow:
            Lnow = Lnext
    else:
        Lans.append(Lnow)
        Rans.append(Rnow)
        Lnow = Lnext
        Rnow = Rnext
    if i == N - 1:
        Lans.append(Lnow)
        Rans.append(Rnow)
ans = sorted(zip(Lans,Rans))

Lans2 = []
Rans2 = []
Lnow2 = ans[0][0]
Rnow2 = ans[0][1]
for i in range(len(ans)):
    if i == 0:
        if len(ans) == 1:
            Lans2.append(Lnow2)
            Rans2.append(Rnow2)
            break
        else:
            continue
    
    Lnext2 = ans[i][0]
    Rnext2 = ans[i][1]
    if  Lnow2 <= Rnext2:
        Rnow = Rnext
        if Lnext <= Lnow:
            Lnow = Lnext
    else:
        Lans.append(Lnow)
        Rans.append(Rnow)
        Lnow = Lnext
        Rnow = Rnext
    if i == N - 1:
        Lans.append(Lnow)
        Rans.append(Rnow)


for valans2 in ans2:
    print(valans2[0], valans2[1])

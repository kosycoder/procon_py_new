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
S = input()
T = input()

scount = []
valSbfr = S[0]
count = 1
for i in range(1,len(S)):
    if S[i] == valSbfr:
        count+=1
    else:
        scount.append([valSbfr, count])
        count = 1
    valSbfr = S[i]
if S[len(S)-1] == S[len(S)-2]:
    scount.append([valSbfr, count])
else:
    scount.append([valSbfr, 1])
DEBUG(scount)

tcount = []
valTbfr = T[0]
count = 1
for i in range(1,len(T)):
    if T[i] == valTbfr:
        count+=1
    else:
        tcount.append([valTbfr, count])
        count = 1
    valTbfr = T[i]
if T[len(T)-1] == T[len(T)-2]:
    tcount.append([valTbfr, count])
else:
    tcount.append([valTbfr, 1])
DEBUG(tcount)

ans = True
if len(scount) != len(tcount):
    ans = False
for i in range(len(scount)):
    nowscount = scount[i]
    nowtcount = tcount[i]

    if nowscount[0] != nowtcount[0]:
        ans = False
        break
    
    if (nowscount[1] == 1 and nowscount[1] != nowtcount[1]) or (nowscount[1] > nowtcount[1]):
        ans = False
        break
YesNo(ans)

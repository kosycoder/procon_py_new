import random
import time

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
s = []
for _ in range(D):
    si = input_intarray()
    s.append(si)

#貪欲法初期値生成
tday = []
score = 0
dlast = [0] * 26
for d in range(D):
    scoretodaymax = int(-1e18)
    alphabettoday = -1
    for alphabettodaytmp in range(26):
        scoretodaytmp = 0
        dlasttodaytmp = []
        for valdlast in dlast:
            dlasttodaytmp.append(valdlast)
        scoretodaytmp += s[d][alphabettodaytmp]
        scoretodaytmp -= c[alphabettodaytmp]*(d+1-dlast[alphabettodaytmp])*(d-dlast[alphabettodaytmp])//2
        dlasttodaytmp[alphabettodaytmp] = d + 1
        for alphabet in range(26):
            scoretodaytmp -= c[alphabet]*(d+2-dlasttodaytmp[alphabet])*(d+1-dlasttodaytmp[alphabet])//2
        if scoretodaytmp >= scoretodaymax:
            scoretodaymax = scoretodaytmp
            alphabettoday = alphabettodaytmp
    dlast[alphabettoday] = d + 1
    score = scoretodaymax
    tday.append(alphabettoday)

##山登り法
starttime = time.time()
cntupdate = 0
cntloop = 0
while(time.time()-starttime<1.8):
    scoretmp = 0
    dlast = [0] * 26
    tdaytmp = []
    for valtday in tday:
        tdaytmp.append(valtday)
    drandom = random.randint(0, D)
    qrandom = random.randint(0, 25)
    tdaytmp[drandom-1] = qrandom
    for d in range(D):
        alphabettoday = tdaytmp[d] - 1
        scoretmp += s[d][alphabettoday]
        scoretmp -= c[alphabettoday]*(d+1-dlast[alphabettoday])*(d-dlast[alphabettoday])//2
        dlast[alphabettoday] = d + 1
    for alphabet in range(26):
        scoretmp -= c[alphabet]*(d+2-dlast[alphabet])*(d+1-dlast[alphabet])//2
    #変更して良くなったらtday更新
    if scoretmp >= score:
        tday = []
        for valtdaytmp in tdaytmp:
            tday.append(valtdaytmp)
        score = scoretmp
        cntupdate += 1
    cntloop += 1

tday = [int(val+1) for val in tday]
for valtday in tday:
    print(valtday)
DEBUG([cntupdate, cntloop])
DEBUG(int(score+1e6))
DEBUG(time.time()-starttime)

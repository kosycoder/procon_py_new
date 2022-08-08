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

def calc_score(X):
    score = 0
    last = [-1] * SIZE
    for day in range(D):
        type = X[day]
        score += s[day][type]
        last[type] = day
        score -= sum(c[j] * (day - last[j]) for j in range(SIZE))
    return score

def prev_day(X, day, type):
    for i in range(day - 1, -1, -1):
        if X[i] == type:
            return i
    return -1

def next_day(X, day, type):
    for i in range(day + 1, D):
        if X[i] == type:
            return i
    return D

def calc_scorediff(X, day, type):
    diff = 0

    # delete X[day]
    diff -= s[day][X[day]]
    prv, nxt = prev_day(X, day, X[day]), next_day(X, day, X[day])
    diff += c[X[day]] * (prv - day) * (nxt - day)

    # insert type
    diff += s[day][type]
    prv, nxt = prev_day(X, day, type), next_day(X, day, type)
    diff += c[type] * (day - prv) * (nxt - day)

    return diff

def greedy():
    t = []
    score0 = 0
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
        score0 = scoretodaymax
        t.append(alphabettoday)
    return t, score0

def hillcliming(t, timelimit):
    starttime = time.time()
    cntupdate = 0
    cntloop = 0
    scorebfr = score0
    while(time.time()-starttime<timelimit):
        drandom = random.randint(0, D-1)
        qrandom = random.randint(0, 25)

        scorediff = calc_scorediff(t, drandom, qrandom)
        scoreaft = scorebfr + scorediff

        #変更して良くなったらtday更新
        if scoreaft > scorebfr:
            t[drandom] = qrandom
            scorebfr = scoreaft
            cntupdate += 1
        cntloop += 1
    return t, scorebfr

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = True

SIZE = 26

D = int(input())
c = input_intarray()
s = []
for _ in range(D):
    si = input_intarray()
    s.append(si)

## 貪欲法で初期値生成
t, score0 = greedy()

## 山登り法で求解
timelimit = 1.8
tans, scoreans = hillcliming(t, timelimit)

## 出力
for valt in t:
    print(valt+1)

DEBUG(int(score0+1e6))
DEBUG(int(scoreans+1e6))

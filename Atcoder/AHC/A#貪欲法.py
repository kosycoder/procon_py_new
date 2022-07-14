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

# tday = []
# for _ in range(D):
#     tday.append(int(input()))

dq = []

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
    score += scoretodaymax
    print(alphabettoday+1)
DEBUG(int(score+1e6))

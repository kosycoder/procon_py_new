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

DEBUGFLG = True

D = int(input())
c = input_intarray()
csum = sum(c)
s = []
for _ in range(D):
    si = input_intarray()
    s.append(si)

tday = []
for _ in range(D):
    tday.append(int(input()))

M = int(input())
dq = []
for _ in range(M):
    di, qi = map(int,input().split())
    dq.append((di, qi))

for m in range(M):
    contestday = dq[m][0] - 1
    contesttypei = tday[contestday] - 1
    tday[contestday] = dq[m][1]
    contesttypej = dq[m][1] - 1

    if m == 0:
        ans = 0
        dlast = [-1] * 26
        ds = [[] for i in range(26)]
        for d in range(D):
            alphabettoday = tday[d] - 1
            ans += s[d][alphabettoday]
            ans -= c[alphabettoday]*(d-dlast[alphabettoday])*(d-dlast[alphabettoday]-1)//2
            dlast[alphabettoday] = d
            ds[alphabettoday].append(d)
        for alphabet in range(26):
            ans -= c[alphabet]*(d+1-dlast[alphabet])*(d-dlast[alphabet])//2
        print(ans)
        DEBUG(ds)
    
    else:
        labelcontestidayd = bisect.bisect_left(ds[contesttypei], contestday)
        labelcontestjdayd = bisect.bisect_left(ds[contesttypej], contestday)

        if labelcontestidayd - 1 == -1:
            dayheldcontestibfrdayd = -1
        else:
            dayheldcontestibfrdayd = ds[contesttypei][labelcontestidayd-1]
        if labelcontestidayd + 1 >= len(ds[contesttypei]):
            dayheldcontestiaftdayd = D
        else:
            dayheldcontestiaftdayd = ds[contesttypei][labelcontestidayd+1]
        if labelcontestjdayd - 1 == -1:
            dayheldcontestjbfrdayd = -1
        else:
            dayheldcontestjbfrdayd = ds[contesttypej][labelcontestjdayd-1]
        if labelcontestjdayd + 1 >= len(ds[contesttypej]):
            dayheldcontestjaftdayd = D
        else:
            dayheldcontestjaftdayd = ds[contesttypej][labelcontestjdayd+1]
        DEBUG(dayheldcontestibfrdayd)
        DEBUG(dayheldcontestiaftdayd)
        DEBUG(dayheldcontestjbfrdayd)
        DEBUG(dayheldcontestjaftdayd)
        
        ans -= s[contestday][contesttypei]
        ans += s[contestday][contesttypej]
        ans += c[contesttypei]*(dayheldcontestibfrdayd-contestday)*(dayheldcontestiaftdayd-contestday)//2
        ans -= c[contesttypej]*(dayheldcontestjbfrdayd-contestday)*(dayheldcontestjaftdayd-contestday)//2
        # ans -= c[contesttypei]*(contestday-dayheldcontestibfrdayd)*(contestday-dayheldcontestibfrdayd-1)//2
        # ans -= c[contesttypei]*(dayheldcontestiaftdayd-contestday)*(dayheldcontestiaftdayd-contestday-1)//2
        # ans += c[contesttypei]*(dayheldcontestiaftdayd-dayheldcontestibfrdayd)*(dayheldcontestiaftdayd-dayheldcontestibfrdayd-1)//2
        # ans += c[contesttypej]*(contestday-dayheldcontestjbfrdayd)*(contestday-dayheldcontestjbfrdayd-1)//2
        # ans += c[contesttypej]*(dayheldcontestjaftdayd-contestday)*(dayheldcontestjaftdayd-contestday-1)//2
        # ans -= c[contesttypej]*(dayheldcontestjaftdayd-dayheldcontestjbfrdayd)*(dayheldcontestjaftdayd-dayheldcontestjbfrdayd-1)//2
        print(ans)

        del ds[contesttypei][labelcontestidayd]
        ds[contesttypej].append(contestday)
        ds[contesttypej] = sorted(ds[contesttypej])
        DEBUG(ds)

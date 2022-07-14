import bisect

def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def My_sort(l, num = 0, revflg = False):
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

N = int(input())
Q = input()
W = input_intarray()

WQ = zip(W,Q)
WQ = sorted(WQ)
DEBUG(WQ)
anstmp = 0
for valq in Q:
    if valq == '1':
        anstmp += 1
DEBUG(anstmp)

ans = anstmp
for i in range(N):
    valWnow = WQ[i][0]
    valQnow = WQ[i][1]
    if valQnow == "0":
        anstmp += 1
    else:
        anstmp -= 1
    if i < len(WQ)-1:
        valWnext = WQ[i+1][0]
        valQnext = WQ[i+1][1]
        if valWnow != valWnext:
            ans = max(ans, anstmp)
    else:
        ans = max(ans, anstmp)
    
print(ans)

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
R, C = map(int,input().split())
if C > 8:
    C = 16 - C
if R > 8:
    R = 16 - R

flg = True
if R == 1:
    pass
elif R == 2:
    if C != 1: 
        flg = False
elif R == 3:
    if C == 2: 
        flg = False
elif R == 4:
    if C != 1 and C!=3: 
        flg = False
elif R == 5:
    if C == 2 or C == 4: 
        flg = False
elif R == 6:
    if C != 1 and C!=3 and C!=5:
        flg = False
elif R == 7:
    if C == 2 or C == 4 or C == 6: 
        flg = False
elif R == 8:
    if C == 2 or C == 4 or C == 6 or C == 8: 
        flg = False

if flg:
    print("black")
else:
    print("white")

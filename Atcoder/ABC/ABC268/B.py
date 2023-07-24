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

S = input()
T = input()

def solve():
    if len(S) > len(T):
        print("No")
        return
    
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    
    print("Yes")

solve()

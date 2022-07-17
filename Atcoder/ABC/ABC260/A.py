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
if S[0] == S[1] == S[2]:
    print(-1)
elif S[0] == S[1]:
    print(S[2])
elif S[1] == S[2]:
    print(S[0])
elif S[0] == S[2]:
    print(S[1])
else:
    print(S[0])

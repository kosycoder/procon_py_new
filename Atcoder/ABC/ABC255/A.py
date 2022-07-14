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
R, C = map(int,input().split())
A11, A12 = map(int,input().split())
A21, A22 = map(int,input().split())
if R == 1 and C == 1:
    print(A11)
elif R == 1 and C == 2:
    print(A12)
elif R == 2 and C == 1:
    print(A21)
elif R == 2 and C == 2:
    print(A22)

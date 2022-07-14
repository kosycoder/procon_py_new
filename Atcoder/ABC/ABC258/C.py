from itertools import accumulate


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

N, Q = map(int,input().split())
S = input()
accum = 0
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        accum -= x
        DEBUG(accum)
    elif t == 2:
        num = (x + accum - 1) % N
        DEBUG(x)
        DEBUG(accum)
        print(S[num])

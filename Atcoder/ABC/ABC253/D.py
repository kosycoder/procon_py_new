from collections import deque

def DEBUG(debugoutput, flg = False):
    if flg:
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

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

S = {}
Q = int(input())
xMAX = -1
xMIN = int(1e18)
for valq in range(Q):
    s = input_intarray()
    num = int(s[0])

    if num == 1:
        x = int(s[1])
        if x in S:
            S[x] += 1
        else:
            S[x] = 1
    elif num == 2:
        x = int(s[1])
        c = int(s[2])
        if x in S:
            S[x] -= min(c,S[x])
            if S[x] == 0:
                S.pop(x)
    elif num == 3:
        print(max(S)-min(S))
    DEBUG(S, DEBUGFLG)

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

L1, R1, L2, R2 = map(int,input().split())

R = [False] * 101
B = [False] * 101
for i in range(L1, R1+1):
    R[i] = True
for i in range(L2, R2+1):
    B[i] = True

ans = 0
for i in range(0,101):
    if R[i] == B[i] == True:
        ans += 1
print(max(ans-1,0))

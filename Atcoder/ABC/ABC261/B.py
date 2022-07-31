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
N = int(input())
# A = [[None]*N for _ in range(N)]
A = []
for i in range(N):
    Ain = input()
    A.append(Ain)

ans = True
for i in range(N):
    for j in range(N):
        if A[i][j] == "W" and A[j][i] != "L":
            ans = False
            break
        if A[i][j] == "L" and A[j][i] != "W":
            ans = False
            break
        if A[i][j] == "D" and A[j][i] != "D":
            ans = False
            break

if ans:
    print("correct")
else:
    print("incorrect")
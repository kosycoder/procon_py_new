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

N, M = map(int,input().split())
matrix = [[False]*N for _ in range(N)]
for _ in range(M):
    ain, bin = map(int,input().split())
    ain -= 1
    bin -= 1
    matrix[ain][bin] = True
Q = int(input())
x = []
k = []
for _ in range(Q):
    xin, kin = map(int,input().split())
    x.append(xin)
    k.append(kin)



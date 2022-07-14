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
A = []
for _ in range(N):   
    A.append(input())

ans = 0
direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
cnt = 0
for y in range(N):
    for x in range(N):
        for valdirection in direction:
            nowx = x
            nowy = y
            anstmp = int(A[y][x])
            dx = valdirection[0]
            dy = valdirection[1]
            for _ in range(N-1):
                nowy += dy
                if nowy == -1:
                    nowy = N-1
                if nowy == N:
                    nowy = 0
                nowx += dx
                if nowx == -1:
                    nowx = N-1
                if nowx == N:
                    nowx = 0
                anstmp *= 10
                anstmp += int(A[nowy][nowx])
            DEBUG(anstmp)
            ans = max(ans, anstmp)
            cnt += 1
DEBUG(cnt)
print(ans)

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
ans = [[] for _ in range(N)]

for i in range(N): 
    for j in range(i+1):
        if j == 0:
            ans[i].append(1)
        elif j == i:
            ans[i].append(1)
        else:
            ans[i].append(ans[i-1][j-1]+ans[i-1][j])
        DEBUG(ans)

for i in range(N):
    print(*ans[i])

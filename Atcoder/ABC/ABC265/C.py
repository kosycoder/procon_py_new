from logging.handlers import WatchedFileHandler


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

H, W,= map(int,input().split())
G = []
for _ in range(H):
    G.append(input())

count = 0
xnow = 0
ynow = 0
while(1):
    if G[ynow][xnow] == "U":
        DEBUG([ynow+1, xnow+1])
        if ynow != 0:
            ynow -= 1
        else:
            print(ynow+1, xnow+1)
            break
    elif G[ynow][xnow] == "D":
        DEBUG([ynow+1, xnow+1])
        if ynow != H-1:
            ynow += 1
        else:
            print(ynow+1, xnow+1)
            break
    elif G[ynow][xnow] == "L":
        DEBUG([ynow+1, xnow+1])
        if xnow != 0:
            xnow -= 1
        else:
            print(ynow+1, xnow+1)
            break
    else:
        DEBUG([ynow+1, xnow+1])
        if xnow != W-1:
            xnow += 1
        else:
            print(ynow+1, xnow+1)
            break
    if count > 1e6:
        print(-1)
        break

    count += 1

from collections import deque

ans = []
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

def solve():
    state = []
    r, c = map(int,input().split())
    blk = [list(map(int,input().split())) for l in range(r)]
    for itrr in range(r):
        state.append([-1]*c)
    for itrr in range(r):
        print(blk[itrr])

    maxblk = 0
    startr = 0
    startc = 0
    for itrr in range(r):
        for itrc in range(c):
            if blk[itrr][itrc] > maxblk:
                maxblk = blk[itrr][itrc]
                startr = itrr
                startc = itrc
    state[startr][startc] = 0

    anstmp = 0
    Q = deque()
    Q.append([startr,startc])
    while len(Q) != 0:
        u = Q.popleft()
        # print(u)
        nowr = u[0]
        nowc = u[1]
        if nowc != 0:
            addblk = max(blk[nowr][nowc]-blk[nowr][nowc-1]-1,0)
            blk[nowr][nowc-1] += addblk
            anstmp += addblk
            if state[nowr][nowc-1] == -1:
                state[nowr][nowc-1] = 0
                Q.append([nowr,nowc-1])
        if nowr != 0:
            addblk = max(blk[nowr][nowc]-blk[nowr-1][nowc]-1,0)
            blk[nowr-1][nowc] += addblk
            anstmp += addblk
            if state[nowr-1][nowc] == -1:
                state[nowr-1][nowc] = 0
                Q.append([nowr-1,nowc])
        if nowc != c-1:
            addblk = max(blk[nowr][nowc]-blk[nowr][nowc+1]-1,0)
            blk[nowr][nowc+1] += addblk
            anstmp += addblk
            if state[nowr][nowc+1] == -1:
                state[nowr][nowc+1] = 0
                Q.append([nowr,nowc+1])
        if nowr != r-1:
            addblk = max(blk[nowr][nowc]-blk[nowr+1][nowc]-1,0)
            blk[nowr+1][nowc] += addblk
            anstmp += addblk
            if state[nowr+1][nowc] == -1:
                state[nowr+1][nowc] = 0
                Q.append([nowr+1,nowc])
        state[nowr][nowc] = 1

    # print("blk")
    # for itrr in range(r):
    #     print(blk[itrr])
    ans.append(anstmp)

def disp(itmp):
    print("Case #",end="")
    print(itmp+1,end="")
    print(": ",end="")
    print(ans[itmp])

t = int(input())
for itr in range(t):
    solve()
for itr in range(t):
    disp(itr)

# 3
# 1 3
# 3 4 3
# 1 3
# 3 0 0
# 3 3
# 0 0 0
# 0 2 0
# 0 0 0


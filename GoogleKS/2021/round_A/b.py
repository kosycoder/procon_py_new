ans = []
def solve():
    r, c = map(int,input().split())
    blk = [input().split() for l in range(r)]

    Su = []
    Sd = []
    Sr = []
    Sl = []
    for itrr in range(r+2):
        Su.append([0]*(c+2))
        Sd.append([0]*(c+2))
        Sl.append([0]*(c+2))
        Sr.append([0]*(c+2))
            
    for itrr in range(r):
        for itrc in range(c):
            if blk[itrr][itrc] == '1':
                Su[itrr+1][itrc+1] = Su[itrr][itrc+1] + 1
    for itrr in range(r):
        for itrc in range(c):
            if blk[itrr][c-itrc-1] == '1':
                Sr[itrr+1][c-itrc] = Sr[itrr+1][c+1-itrc] + 1
    for itrc in range(c):
        for itrr in range(r):
            if blk[itrr][itrc] == '1':
                Sl[itrr+1][itrc+1] = Sl[itrr+1][itrc] + 1
    for itrc in range(c):
        for itrr in range(r):
            if blk[r-itrr-1][itrc] == '1':
                Sd[r-itrr][itrc+1] = Sd[r+1-itrr][itrc+1] + 1
            
    anstmp = 0
    for itrr in range(r):
        for itrc in range(c):
            if Su[itrr+1][itrc+1] >= 2 and Sr[itrr+1][itrc+1] >= 2:
                anstmp += min(Su[itrr+1][itrc+1]//2,Sr[itrr+1][itrc+1])-1
                anstmp += min(Sr[itrr+1][itrc+1]//2,Su[itrr+1][itrc+1])-1
            if Su[itrr+1][itrc+1] >= 2 and Sl[itrr+1][itrc+1] >= 2:
                anstmp += min(Su[itrr+1][itrc+1]//2,Sl[itrr+1][itrc+1])-1
                anstmp += min(Sl[itrr+1][itrc+1]//2,Su[itrr+1][itrc+1])-1
            if Sd[itrr+1][itrc+1] >= 2 and Sr[itrr+1][itrc+1] >= 2:
                anstmp += min(Sd[itrr+1][itrc+1]//2,Sr[itrr+1][itrc+1])-1
                anstmp += min(Sr[itrr+1][itrc+1]//2,Sd[itrr+1][itrc+1])-1
            if Sd[itrr+1][itrc+1] >= 2 and Sl[itrr+1][itrc+1] >= 2:
                anstmp += min(Sd[itrr+1][itrc+1]//2,Sl[itrr+1][itrc+1])-1
                anstmp += min(Sl[itrr+1][itrc+1]//2,Sd[itrr+1][itrc+1])-1
    
    ans.append(anstmp)
    # print("blk")
    # for itrr in range(r):
    #     print(blk[itrr])
    # print("Su")
    # for itrr in range(r+2):
    #     print(Su[itrr])
    # print("Sd")
    # for itrr in range(r+2):
    #     print(Sd[itrr])
    # print("Sl")
    # for itrr in range(r+2):
    #     print(Sl[itrr])
    # print("Sr")
    # for itrr in range(r+2):
    #     print(Sr[itrr])

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

# 1
# 4 3
# 1 0 0
# 1 0 1
# 1 0 0
# 1 1 0

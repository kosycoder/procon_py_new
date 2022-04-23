n = int(input())

xy = [list(map(int,input().split())) for l in range(n)]

ans = 0
for itrn in range(n):
    for itr in list(range(itrn,n,1)):
        anstmp = (xy[itrn][0] - xy[itr][0])**2 + (xy[itrn][1] - xy[itr][1])**2
        ans = max(ans, anstmp)

print(ans**0.5)

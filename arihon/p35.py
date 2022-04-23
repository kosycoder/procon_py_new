n = int(input())
m = int(input())
garden = [list(input()) for l in range(n)]

def func(ntmp, mtmp):
    if garden[ntmp][mtmp] == "W":
        garden[ntmp][mtmp] = "."
        if ntmp != 0 and mtmp != 0:
            func(ntmp-1,mtmp-1)
        if ntmp != 0:
            func(ntmp-1,mtmp)
        if ntmp != 0 and mtmp != m-1:
            func(ntmp-1,mtmp+1)
        if mtmp != 0:
            func(ntmp,mtmp-1)
        if mtmp != m-1:
            func(ntmp,mtmp+1)
        if ntmp != n-1 and mtmp != 0:
            func(ntmp+1,mtmp-1)
        if ntmp != n-1:
            func(ntmp+1,mtmp)
        if ntmp != n-1 and mtmp != m-1:
            func(ntmp+1,mtmp+1)

ans = 0
for itrn in range(n):
    for itrm in range(m):
        if garden[itrn][itrm] == "W":
            ans += 1
            func(itrn,itrm)
        else:
            continue

print(ans)

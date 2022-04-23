import bisect

n = int(input())
a = input().split()
a = [int(i) for i in a]
b = input().split()
b = [int(i) for i in b]
c = input().split()
c = [int(i) for i in c]
d = input().split()
d = [int(i) for i in d]

def solve():
    cd = []
    for i in range(n):
        for j in range(n):
            cd.append(c[i]+d[j])
    cd = sorted(cd)

    ans = 0
    for i in range(n):
        for j in range(n):
            ab = -a[i]-b[j]
            ans += bisect.bisect_right(cd,ab) - bisect.bisect_left(cd,ab)
    
    print(ans)

solve()

# 6
# -45 -41 -36 -36 26 -32
# 22 -27 53 30 -38 -54
# 42 56 -37 -75 -10 -6
# -16 30 77 -46 62 45

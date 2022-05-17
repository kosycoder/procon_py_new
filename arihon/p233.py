import bisect

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

def comp(px, py, qx, qy):
    if px != qx:
        return px < qx
    return py < qy

def convex_hull(ps, n):
    k = 0
    ps = sorted(ps, key=comp(ps))
    return ps

def calc_distance_squared(px, py, qx, qy):
    return (px - qx) ** 2 + (py - qy) ** 2

N = int(input())

x = []
y = []
for _ in range(N):
    xin, yin = map(int,input().split())
    x.append(xin)
    y.append(yin)
xy = [x, y]
print(xy)
print(convex_hull(xy, N))

# 8
# 0 5
# 1 8
# 3 4
# 5 0
# 6 2
# 6 6
# 8 3
# 8 7

from collections import deque

def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

EPS = 1e-10

n = int(input())
p = []
for i in range(n):
    px, py = map(int,input().split())
    p.append([px, py])
q = []
for i in range(n):
    qx, qy = map(int,input().split())
    q.append([qx, qy])
m = int(input())
ab = []
for i in range(n):
    a, b = map(int,input().split())
    ab.append([a-1, b-1])

def doubleadd(a, b):
    if abs(a + b) < EPS * (abs(a) + abs(b)):
        return 0
    return a + b

def dotproduct(p1x, p1y, p2x, p2y):
    return doubleadd(p1x * p2x, p1y * p2y)

def crossproduct(p1x, p1y, p2x, p2y):
    return doubleadd(p1x * p2y, -p2x * p1y)

def on_seg(p1x, p1y, p2x, p2y, qx, qy):
    return crossproduct(p1x-qx, p1y-qy, p2x-qx, p2y-qy)==0 and dotproduct(p1x-qx, p1y-qy, p2x-qx, p2y-qy)<=0

def intersection(p1x, p1y, p2x, p2y, q1x, q1y, q2x, q2y):
    numerator = crossproduct(q2x-q1x, q2y-q1y, q1x-p1x, q1y-p1y)
    denominator = crossproduct(q2x-q1x, q2y-q1y, p2x-p1x, p2y-p1y)
    ansx = doubleadd(p1x, numerator / denominator * doubleadd(p2x, -p1x))
    ansy = doubleadd(p1y, numerator / denominator * doubleadd(p2y, -p1y))

    return ansx, ansy

g = [[False] * n for _ in range(n)]
def solve():
    for i in range(n):
        g[i][i] = True
        for j in range(n):
            pix = p[i][0]
            piy = p[i][1]
            qix = q[i][0]
            qiy = q[i][1]
            pjx = p[j][0]
            pjy = p[j][1]
            qjx = q[j][0]
            qjy = q[j][1]
            if crossproduct(pix-qix, piy-qiy, pjx-qjx, pjy-qjy) == 0:
                g[i][j] = on_seg(pix, piy, qix, qiy, pjx, pjy) or \
                    on_seg(pix, piy, qix, qiy, qjx, qjy) or \
                    on_seg(pjx, pjy, qjx, qjy, pix, piy) or \
                    on_seg(pjx, pjy, qjx, qjy, qix, qiy)
                g[j][i] = g[i][j]
            else:
                rx, ry = intersection(pix, piy, qix, qiy, pjx, pjy, qjx, qjy)
                g[i][j] = on_seg(pix, piy, qix, qiy, rx, ry) and on_seg(pjx, pjy, qjx, qjy, rx, ry)
                g[j][i] = g[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = g[i][j] or g[i][k] and g[k][j]
    
    for i in range(m):
        if g[ab[i][0]][ab[i][1]]:
            print("CONNECTED")
        else:
            print("NOT CONNECTED")

solve()

# 4
# 0 4
# 0 1
# 1 2
# 1 0
# 4 1
# 2 3
# 3 4
# 2 1
# 4
# 1 2
# 1 4
# 2 3
# 2 4
print(g)
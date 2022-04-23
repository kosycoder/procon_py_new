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

w, h, n = map(int,input().split())
x1 = input_intarray()
x2 = input_intarray()
y1 = input_intarray()
y2 = input_intarray()

def compress(p1, p2, wth):
    ps = set()

    for i in range(n):
        for d in [-1,0,1]:
            tp1, tp2 = p1[i] + d, p2[i] + d
            if 1 <= tp1 <= wth:
                ps.add(tp1)
            if 1 <= tp2 <= wth:
                ps.add(tp2)
    ps = sorted(list(ps))
    p1 = [ps.index(p1[i]) for i in range(n)]
    p2 = [ps.index(p2[i]) for i in range(n)]
    return p1, p2, len(ps)

x1, x2, w = compress(x1, x2, w)
y1, y2, h = compress(y1, y2, h)

fld = [[False] * (6*n) for _ in range(6*n)]
for i in range(n):
    for y in range(y1[i], y2[i]+1):
        for x in range(x1[i], x2[i]+1):
            fld[y][x] = True

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0
for y in range(h):
    for x in range(w):
        if fld[y][x]:
            continue
        
        ans += 1
        queue = deque()
        queue.append([x,y])
        while len(queue):
            sx, sy = queue.popleft()
            for i in range(4):
                tx, ty = sx + dx[i], sy + dy[i]
                if tx < 0 or w <= tx or ty < 0 or h <= ty:
                    continue
                if fld[ty][tx]:
                    continue
                queue.append([tx,ty])
                fld[ty][tx] = True

print(ans)

# 10 10 5
# 1 1 4 9 10
# 6 10 4 9 10
# 4 8 1 1 6
# 4 8 10 5 10

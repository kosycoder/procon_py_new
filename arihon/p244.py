import math

def DEBUG(debugoutput, flg = False):
    if flg:
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

# dx, dy = [-1, -1, 1, 1], [-1, 0, -1, 0]

DEBUGFLG = False

N = int(input())

X = []
Y = []
R = []
for _ in range(N):
    xin, yin, rin = map(float,input().split())
    X.append(xin)
    Y.append(yin)
    R.append(rin)

DEBUG(X,DEBUGFLG)

def cover(x, y, r):
    S = 0
    for i in range(N):
        if R[i] <= r:
            dx = x - X[i]
            dy = y - Y[i]
            dr = r - R[i]
        if dx * dx + dy * dy <= dr * dr:
            S |= (1<<i)
    
    return S

def check(r):
    cand = [0]

    for i in range(N):
        for j in range(i):
            if R[i] < r and R[j] < r:
                x1 = X[i]
                y1 = Y[i]
                r1 = r - R[i]
                x2 = X[j]
                y2 = Y[j]
                r2 = r - R[j]
                dx = x2 - x1
                dy = y2 - y1
                a = dx * dx + dy * dy
                b = ((r1 * r1 - r2 * r2) / a + 1) / 2
                d = r1 * r1 / a - b * b
                if d >= 0:
                    d = math.sqrt(d)
                    x3 = x1 + dx * b
                    y3 = y1 + dy * b
                    x4 = -dy * d
                    y4 = dx * d
                    ij = 1<<i | 1<<j
                    cand.append(cover(x3-x4, y3-y4, r) | ij)
                    cand.append(cover(x3+x4, y3+y4, r) | ij)
    
    for i in range(N):
        if R[i] <= r:
            cand.append(cover(X[i], Y[i], r) | (1 << i))
    
    for i in range(len(cand)):
        for j in range(i):
            if ((cand[i] | cand[j]) == (1<<N) - 1):
                return True
    return False

def solve():
    lb = 0.0
    ub = 10000.0
    for i in range(100):
        mid = (lb + ub) / 2
        if check(mid):
            ub = mid
        else:
            lb = mid

    print(ub)

solve()

# 3
# 20 10 2
# 20 20 2
# 40 10 3

# 3
# 20 10 3
# 30 10 3
# 40 10 3


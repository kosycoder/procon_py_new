import math

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

N = int(input())
V = int(input())
X, Y = map(int, input().split())
L = []
B = []
R = []
T = []
for _ in range(N):
    l, b, r, t = map(int,input().split())
    L.append(l)
    B.append(b)
    R.append(r)
    T.append(t)
    
g = 9.8
EPS = 1e-10

def calc(vy, t):
    return vy * t - g / 2 * t * t

def cmp(lb, ub, a):
    if a < lb + EPS:
        ans = -1
    else:
        if a > ub - EPS:
            ans = 1
        else:
            ans = 0

    return ans

def check(qx, qy):
    a = g * g / 4
    b = g * qy - V * V
    c = qx * qx + qy * qy
    D = b * b - 4 * a * c
    if D < 0 and D > -EPS:
        D = 0
    
    if D < 0:
        return False
    
    for sign in [-1,1]:
        t2 = (-b + sign * math.sqrt(D)) / 2 / a
        if t2 <= 0:
            continue
        t = math.sqrt(t2)
        vx = qx / t
        vy = (qy + g * t * t / 2) / t

        yt = calc(vy, X/vx)
        if yt < Y - EPS:
            continue

        flg = True
        for i in range(N):
            if L[i] >= X:
                continue
            if R[i] == X and Y <= T[i] and B[i] <= yt:
                flg = False
            yL = cmp(B[i], T[i], calc(vy, L[i]/vx))
            yR = cmp(B[i], T[i], calc(vy, R[i]/vx))
            xH = cmp(L[i], R[i], vx * (vy / g))
            yH = cmp(B[i], T[i], calc(vy, vy / g))
            if xH == 0 and yH >= 0 and yL < 0:
                flg = False
            if yL * yR <= 0:
                flg = False
        if flg:
            return True

    return False

def solve():
    for i in range(N):
        R[i] = min(R[i], X)
    
    flg = check(X, Y)

    for i in range(N):
        flg |= check(L[i], T[i])
        flg |= check(R[i], T[i])
    
    YesNo(flg)

solve()

# 0
# 7
# 3 1

# 1
# 7
# 3 1
# 1 1 2 2

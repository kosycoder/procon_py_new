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

N, C = map(int,input().split())
L = input_intarray()
S = input_intarray()
A = input_intarray()

ST_SIZE = 1 << 15 - 1
MAX_NC = int(1e4)
M_PI = math.pi

vx = [0] * ST_SIZE
vy = [0] * ST_SIZE
ang = [0] * ST_SIZE
prv = [0] * MAX_NC

def init(k, l, r):
    ang[k] = vx[k] = 0.0

    if r - l == 1:
        vy[k] = L[l]
    else:
        chl = k * 2 + 1
        chr = k * 2 + 2
        init(chl, l, (l+r)//2)
        init(chr, (l+r)//2, r)
        vy[k] = vy[chl] + vy[chr]

def change(s, a, v, l, r):
    if s <= l:
        return
    elif s < r:
        chl = v * 2 + 1
        chr = v * 2 + 2
        m = (l + r) // 2
        change(s, a, chl, l, m)
        change(s, a, chr, m, r)
        if s <= m: 
            ang[v] += a
        s = math.sin(ang[v])
        c = math.cos(ang[v])
        vx[v] = vx[chl] + (c*vx[chr] - s*vy[chr])
        vy[v] = vy[chl] + (s*vx[chr] + c*vy[chr])

def solve():
    init(0, 0, N)
    for i in range(1, N):
        prv[i] = M_PI
    
    for i in range(C):
        s = S[i]
        a = A[i] / 360.0 * 2 * M_PI
        change(s, a-prv[s], 0, 0, N)
        prv[s] = a

        print(vx[0], vy[0])

solve()

# 2 1
# 10 5
# 1
# 90

# 3 2
# 5 5 5
# 1 2
# 270 90

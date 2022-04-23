import typing

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

vx = [] * ST_SIZE
vy = [] * ST_SIZE
ang = [] * ST_SIZE
prv = [] * MAX_NC

def init(k, l, r):
    ang[k] = vx[k] = 0.0

    if r - 1 == 1:
        vy[k] = L[l]
    else:
        chl = k * 2 + 1
        chr = k * 2 + 2
        init(chl, l, (l+r)//2)
        init(chr, (l+r)//2, r)
        vy[k] = vy[chl] + vy[chr]

def change(s, a, v, l, r):
    if s<=1:
        return
    elif s < r:
        chl = v * 2 + 1
        chr = v * 2 + 2
        m = (l + r) // 2
        change(s, a, chl, l, m)
        change(s, a, chr, m, r)
        if s<= m: 
            ang[v] += a
        s = sin(ang[v])
        c = cos(ang[v])
        vx[v] = vx[chl] + (c*vx[chr] - s*vy[chr])


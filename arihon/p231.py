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

N = int(input())

x = []
y = []
r = []
for _ in range(N):
    xin, yin, rin = map(float,input().split())
    x.append(xin)
    y.append(yin)
    r.append(rin)

def inside(i, j):
    dx = x[i] - x[j]
    dy = y[i] - y[j]
    
    return dx * dx + dy * dy <= r[j] * r[j]

def solve():
    events = []
    for i in range(N):
        events.append([x[i]-r[i], i])
        events.append([x[i]+r[i], i+N])
    events = sort(events)

    outers = []
    res = []
    for i in range(len(events)):
        id = events[i][1] % N
        if events[i][1] < N:
            it = bisect.bisect_left(outers, [y[id], id])
            if it != len(outers)-1 and inside(id, it[1]):
                continue
            if it != 0 and inside(id, it[1]):
                continue
            res.push_back(id)
            outers.popitem([y[id], id])
        else:
            outers.popitem([y[id], id])
    
    sort(events)
    print(len(res))
    for i in range(len(res)):
        if i + 1 == len(res):
            print(res[i])
        else:
            print(res[i], end=" ")

solve()

# 5
# 0 -2 1
# 0 3 3
# 0 0 10
# 0 1.5 1
# 50 50 10

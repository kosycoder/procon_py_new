import bisect


def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

n = int(input())
w = input_intarray()
v = input_intarray()
W = int(input())

def solve():
    wvfront = []
    nhalf = n // 2
    for i in range(1<<nhalf):
        sw, sv = 0, 0
        for j in range(nhalf):
            if i >> (j & 1):
                sw += w[j]
                sv += v[j]
        wvfront.append([sw,sv])

    wvfront = sorted(wvfront)
    m = 1
    i = 1
    for i in range(1,1<<nhalf):
        if wvfront[m-1][1] < wvfront[i][1]:
            wvfront[m] = wvfront[i]
            m += 1
    
    ans = 0
    for i in range(1<<(n-nhalf)):
        sw, sv = 0, 0
        for j in range(n-nhalf):
            if i >> j & 1:
                sw += w[j+nhalf]
                sv += v[j+nhalf]
        if sw <= W:
            tvp = bisect.bisect_left(wvfront, [W-sw,float("inf")], hi = m)
            ans = max(ans, sv + wvfront[tvp-1][1])
    print(ans)

solve()

# 4
# 2 1 3 2
# 3 2 4 2
# 5 

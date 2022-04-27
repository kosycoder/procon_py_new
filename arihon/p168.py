from bisect import bisect, bisect_left, bisect_right


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

ST_SIZE = (1<<18)-1

N, M = map(int,input().split())
A = list(map(int,input().split()))
Q = [list(map(int,input().split())) for _ in range(M)]

dat = [[] for _ in range(ST_SIZE)] 

def init(k, l, r):
    if r - l == 1:
        dat[k] = list([A[l]])
    else:
        lch = k*2+1
        rch = k*2+2
        init(lch, l, (l+r)//2)
        init(rch, (l+r)//2, r)
        dat[k] = list(dat[lch])
        dat[k].extend(dat[rch])

def query(i, j, x, k, l, r):
    if j <= l or r <= i:
        return 0
    elif i <= l and r <= j:
        return bisect_right(dat[k], x)
    else:
        lc = query(i, j, x, k*2+1, l, (l+r)//2)
        rc = query(i, j, x, k*2+2, (l+r)//2, r)
        return lc + rc

def solve():
    nums = [0] * N
    for i in range(N):
        nums[i] = A[i]
    nums = sorted(nums)

    init(0, 0, N)

    for i in range(M):
        print("------------")
        l = Q[i][0]
        r = Q[i][1]+1
        k = Q[i][2]

        lb = -1
        ub = N - 1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            c = query(l, r, nums[mid], 0, 0, N)
            if c >= k:
                ub = mid
            else:
                lb = mid
            print(nums[mid])
        
        print(nums[ub])

solve()

# 7 3
# 1 5 2 6 3 7 4
# 2 5 3
# 4 4 1
# 1 7 3

import bisect

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

def divisor(n):
    n = int(n)
    res = []
    i = 1
    while(1):
        if i * i > n:
            break
        if n % i == 0:
            res.append(i)
            if i != n / i:
                res.append(int(n / i))
        i += 1

    return res

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

MAX_N = int(2e5+1)

N = int(input())
A = input_intarray()

DIV = [[] for _ in range(MAX_N+1)]
for i in range(0,MAX_N+1):
    if i == 0:
        continue
    DIV[i] = divisor(i)

CNT = [0] * (MAX_N+1)
for valA in A:
    CNT[valA] += 1 

ans = 0
for valA in A:
    nowDIV = DIV[valA]
    for i in range(len(nowDIV)):
        b = nowDIV[i]
        c = valA // b
        ans += CNT[b] * CNT[c]

print(ans)

n = int(input())
q = input()
dir = []
for valq in q:
    if valq == "F":
        dir.append(0)
    else:
        dir.append(1)

def calc(k):
    f = [0] * 5001
    res = 0
    sum = 0
    i = 0
    while i + k <= n:
        if (dir[i]+sum) % 2 != 0:
            res += 1
            f[i] = 1
        sum += f[i]
        if i - k + 1 >= 0:
            sum -= f[i-k+1]
        i += 1
    
    i = n - k + 1
    while i < n:
        if (dir[i] + sum) % 2 != 0:
            return -1
        if i - k + 1 >= 0:
            sum -= f[i-k+1]
        i += 1
    return res
        
def solve():
    k = 1
    m = n

    j = 1
    while j <= n:
        p = calc(j)
        if p >= 0 and m > p:
            m = p
            k = j
        j += 1

    print(k)
    print(m)
    
solve()

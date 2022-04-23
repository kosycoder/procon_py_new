import bisect

q = int(input())
que = []
array = []
query = []
for i in range(q):
    que = list(input().split())
    que = [int(i) for i in que]
    query.append(que)
    array.append(que[1])
b = sorted(set(array))
dict = {v:i for i, v in enumerate(b)}
d = list(map(lambda v: dict[v], array))
d = [i+1 for i in d]
n = max(d)+1
bit = [0] * (n+1)
print(d)
print(b)

def bitsum(i):
    s = 0
    while i>0:
        s += bit[i]
        i -= i & -i
    return s

def bitadd(i, x):
    while(i<=n):
        bit[i] += x
        i += i & -i

def solve():
    for i in range(q):
        if query[i][0] == 1:
            x_comp = d[i]
            bitadd(x_comp, 1)
        elif query[i][0] == 2:
            x_comp = d[i]
            k = query[i][2]
            l = 1
            r = n
            while(1):
                m = int((l + r)/2)
                if bitsum(x_comp) - bitsum(m-1) >= k:
                    r = m
                else:
                    l = m+1
                if l>r:
                    break
            print(d[m])
        elif query[i][0] == 3:
            x_comp = d[i]
            k = query[i][2]
            l = 1
            r = n
            while(1):
                m = int((l + r)/2)
                if bitsum(m) - bitsum(x_comp-1) >= k:
                    l = m+1
                else:
                    r = m
                if l>r:
                    break
            print(d[m])

solve()

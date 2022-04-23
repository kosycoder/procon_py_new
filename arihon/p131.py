n = int(input())
m = int(input())
x = list(input().split())
x = [int(i) for i in x]
x = sorted(x)

def flg(d):
    last = 0
    for i in range(m-1):
        crt = last + 1
        while crt < n and x[crt] - x[last] < d:
            crt += 1
        if crt == n:
            return False
        last = crt
    return True

lb = 0
rb = int(1e9)
while rb - lb > 1:
    mb = (lb + rb) // 2
    if flg(mb):
        lb = mb
    else:
        rb = mb

print(lb)

# 5
# 3
# 1 2 8 4 9

a, b = map(int, input().split())

def Euclid(p, q):
    if p < q:
        p, q = q, p
    
    if q == 0:
        return p
    else:
        return Euclid(q, p%q)

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

if Euclid(a, b) == 1:
    d, x, y = extgcd(a, b)

    if x > 0:
        print(x, 0, end=" ")
    else:
        print(0, -x, end=" ")

    if y > 0:
        print(y, 0)
    else:
        print(0, -y)
else:
    print(-1)


# 4 11

# 3 0 0 1

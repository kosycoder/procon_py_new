x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

def Euclid(p, q):
    if p < q:
        p, q = q, p
    
    if q == 0:
        return p
    else:
        return Euclid(q, p%q)

if x1 == x2 and y1 == y2:
    print(0)
else:
    print(Euclid(abs(y2-y1), abs(x2-x1)) - 1)

# 1 11
# 5 3

# 3

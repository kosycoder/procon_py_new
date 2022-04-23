n = int(input())
k = int(input())
l = list(input().split())
l = [float(i) for i in l]

lb = 0.0
rb = float(max(l))

while rb - lb > 0.001:
    mb = (lb + rb) / 2
    num = 0
    for lval in l:
        num += lval // mb
    
    if num >= k:
        lb = mb
    else:
        rb = mb
print(rb)

# 4
# 11
# 8.02 7.43 4.57 5.39

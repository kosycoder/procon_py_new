n = int(input())
a = list(input().split())
a = [int(i) for i in a]
k = int(input())

l = -1
r = n
while r - l > 1:
    m = (l + r) // 2
    if a[m] < k:
        l = m
    else:
        r = m

print(r)

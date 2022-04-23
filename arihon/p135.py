n = int(input())
s = int(input())
a = list(input().split())
a = [int(i) for i in a]
print(a)

res = n + 1

i = 0
j = 0
sum = 0

while 1:
    while j < n and sum < s:
        sum += a[j]
        j += 1
    if sum < s:
        break
    res = min(res, j-i)
    sum -= a[i]
    i += 1

if res == n+1:
    res = 0

print(res)

# 10
# 15 
# 5 1 3 5 10 7 4 9 2 8

# 5
# 11
# 1 2 3 4 5

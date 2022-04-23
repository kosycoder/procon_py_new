p = int(input())
a = list(input().split())
a = [int(i) for i in a]
print(a)

dic1 = {}
for vala in a:
    if vala in dic1:
        dic1[vala] += 1
    else:
        dic1[vala] = 1

n = 0
for _ in dic1:
    n += 1

res = p
i = 0
j = 0
num = 0
dic2 = {}
while 1:
    while j < p and num < n:
        if a[j] in dic2:
            dic2[a[j]] += 1
        else:
            dic2[a[j]] = 1
            num += 1
        j += 1
    if num < n:
        break
    res = min(res, j - i)
    dic2[a[i]] -= 1
    if dic2[a[i]] == 0:
        num -= 1
    i += 1

print(res)

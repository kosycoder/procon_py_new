n, m = map(int,input().split())
a = list(input().split())
a = [int(i) for i in a]
b = list(input().split())
b = [int(i) for i in b]

p ={}
for i in a:
    if i-1 in p:
        p[i-1] += 1
    else:
        p[i-1] = 1
    
ans = True
for i in b:
    if i-1 in p:
        p[i-1] -= 1
    else:
        ans = False
        break
    if p[i-1] < 0:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")

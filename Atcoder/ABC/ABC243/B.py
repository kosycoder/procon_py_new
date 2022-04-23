from collections import deque


n = int(input())
a = list(input().split())
a = [int(i) for i in a]
b = list(input().split())
b = [int(i) for i in b]

ans1 = 0
ans2 = 0

for i in range(n):
    if a[i] == b[i]:
        ans1 += 1

a = sorted(a)
b = sorted(b)
a = deque(a)
b = deque(b)
while len(a) != 0 and len(b) != 0:
    if a[0] == b[0]:
        ans2 += 1
        a.popleft()
        b.popleft()
    elif a[0] < b[0]:
        a.popleft()
    else:
        b.popleft()
ans2 = ans2 - ans1
print(ans1)
print(ans2)

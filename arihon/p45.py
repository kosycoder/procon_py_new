from audioop import reverse
from collections import deque

n = int(input())
s = str(input())
t = s[::-1]
ans = []
# print(s)
# print(t)

S = deque()
T = deque()
for i in range(n):
    S.append(s[i])
    T.append(s[n-i-1])

for itr in range(n):
    print(S)
    if S < T:
        c = S.popleft()
        T.pop()
    else:
        c = S.pop()
        T.popleft()
    ans.append(c)

print(ans)

# 6
# ACDBCB

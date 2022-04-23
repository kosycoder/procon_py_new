n = int(input())
s = list(input().split())
t = list(input().split())
s = [int(l) for l in s]
t = [int(l) for l in t]

st = sorted(zip(t,s))
print(st)

ans = 0
nowtime = 0
for i in range(n):
    if nowtime < st[i][1]:
        ans += 1
        nowtime = st[i][0]

print(ans)

# 5
# 1 2 4 6 8
# 3 5 7 9 10

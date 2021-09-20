n = int(input())
a = list(map(int, input().split()))

q = []
cnt = 0
bfr = -1
for now in a:
    if(bfr<now):
        cnt += 1
    else:
        q.append(cnt)
        cnt = 1
    bfr = now
q.append(cnt)

ans = 0
for num in q:
    ans += num*(num+1)/2

print(int(ans))

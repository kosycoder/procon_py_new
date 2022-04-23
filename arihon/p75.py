import heapq

n = int(input())
l = list(map(int,input().split()))

heapq.heapify(l)

if len(l) == 1:
    print(l[0])
else:
    ans = 0
    while 1:
        l1 = heapq.heappop(l)
        l2 = heapq.heappop(l)
        lp = l1 + l2
        ans += lp
        heapq.heappush(l, lp)
        if len(l) == 1:
            break

print(ans)

# 3
# 8 5 8

# 5
# 1 2 3 4 5

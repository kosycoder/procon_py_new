import heapq
n, k = map(int,(input().split()))
p = list(map(int,(input().split())))

q = p[0:k]
print(min(q))
heapq.heapify(q)

for itr in range(k,n):
    m = heapq.heappop(q)
    m = max(m, p[itr])
    heapq.heappush(q,m)
    ans = heapq.heappop(q)
    print(ans)
    heapq.heappush(q, ans)

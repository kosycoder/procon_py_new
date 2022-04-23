import heapq

n = int(input())
l = int(input())
p = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

tank = p
gasstation = 0
gas = []
heapq.heapify(gas)
ans = 0
for i in range(1,l+1):
    tank -= 1
    if gasstation < n:
        if a[gasstation] == i:
            heapq.heappush(gas, a[gasstation])
            gasstation += 1
    if tank == 0:
        if len(gas) == 0:
            print(-1)
            break
        else:
            tank += heapq.heappop(gas)
            ans += 1
print(ans)

# 4
# 25
# 10
# 10 14 20 21
# 10 5 2 4

INF = int(1e9)

n = int(input())
ml = int(input())
md = int(input())

ld = []
for i in range(n-1):
    ld.append([i+1, i, 0])

for _ in range(ml):
    al, bl, dl = map(int, input().split())
    al -= 1
    bl -= 1
    ld.append([al, bl, dl])

for _ in range(md):
    ad, bd, dd = map(int, input().split())
    ad -= 1
    bd -= 1
    ld.append([bd, ad, -dd])

def BellmanFord(s):
    dist = [INF] * n
    dist[s] = 0
    while (True):
        update = False
        for i in range(n-1+ml+md):
            a, b, d = ld[i]
            if (dist[a] != INF and dist[b] > dist[a] + d):
                dist[b] = dist[a] + d
                update = True
        if update == False:
            break

    if d[0] < 0:
        return -1
    elif d[n-1] == INF:
        return -2
    else:
        return dist[n-1]

print(BellmanFord(0))

# 4
# 2
# 1
# 1 3 10
# 2 4 20
# 2 3 3

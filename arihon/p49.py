n = int(input())
l = list(input().split())
l = [int(numl) for numl in l]

if n == 1:
    print(l[0])
elif n == 2:
    print(l[0]+l[1])
else:
    ans = 0
    min1idx = 0
    min2idx = 1
    while(n>1):
        if l[min1idx] > l[min2idx]: 
            min1idx, min2idx = min2idx, min1idx
        for i in range(2,n):
            if l[i] < l[min1idx]:
                min2idx = min1idx
                min1idx = i
            elif l[i] < l[min2idx]:
                min2idx = i
        t = l[min1idx] + l[min2idx]
        ans += t

        if min1idx == n - 1: min1idx, min2idx = min2idx, min1idx
        l[min1idx] = t
        l[min2idx] = l[n-1]
        n -= 1

    print(ans)

# 3
# 8 5 8

# 5
# 1 2 3 4 5

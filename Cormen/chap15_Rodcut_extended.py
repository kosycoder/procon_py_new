n = int(input())
p = []
p.append(0)
pin = list(map(int,input().split()))
p = p + pin
r = [-10000]*(n+1)
s = [-1]*(n+1)
r[0] = 0

for itrj in range(1,n+1):
    for itri in range(1,n+1):
        if r[itrj] < p[itri]+r[itrj-itri]:
            r[itrj] = p[itri]+r[itrj-itri]
            s[itrj] = itri
            
print(r)
print(s)

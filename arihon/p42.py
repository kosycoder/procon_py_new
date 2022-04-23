c = list(input().split())
c = [int(s) for s in c]
a = int(input())

ans =[0]*6
money = [1,5,10,50,100,500]

for i in [5,4,3,2,1,0]:
    ans[i] = min(a//money[i], c[i])
    a -= money[i]*ans[i]
    if a == 0:
        print(sum(ans))
        break

# 3 2 1 3 0 2
# 620

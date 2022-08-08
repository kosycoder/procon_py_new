def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

def divisor(n):
    n = int(n)
    res = []
    i = 1
    while(1):
        if i * i > n:
            break
        if n % i == 0:
            res.append(i)
            if i != n / i:
                res.append(int(n / i))
        i += 1

    return res

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N = int(input())
ans = 0
for i in range(1,N+1):
    k = i
    d = 2
    while d*d<=k:
        while k%(d*d)==0:
            k /= d * d
        d += 1
    
    d = 1
    while (k*d*d<=N):
        ans += 1
        d += 1

print(ans)



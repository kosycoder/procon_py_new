def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 素数判定
def is_prime(n):
    n = int(n)
    i = 2
    while(1):
        if i * i > n:
            break
        if n % i == 0:
            return False
        i += 1

    return n != 1

def sieve(n):
    is_prime = [True] * (n+1)
    prime = []
    p = 0
    is_prime[0] = is_prime[1] = False
    i = 2
    for i in range(2,n+1):
        if is_prime[i]:
            p += 1
            prime.append(i)
            j = 2 * i
            while 1:
                if j > n:
                    break
                is_prime[j] = False
                j += i
    return p

N = int(input())

primenums = []
cnt = 1
for i in range(1,int(1e6)+1):
    if is_prime(i):
        primenums.append([i,cnt])
        cnt += 1

ans = 0
for i in range(1,len(primenums)):
    q3 = primenums[i][0]**3
    if 2*q3 > N:
        break
    
    l = 0
    r = len(primenums)-1
    while l < r:
        mid = (l+r)//2
        if primenums[mid][0] <= min(primenums[i][0]-1, N//q3):
            l = mid + 1
        else:
            r = mid
    p = primenums[l-1][1]
    # print(p, q3, l)
    ans += p

print(ans)

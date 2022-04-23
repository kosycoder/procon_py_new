n = int(input())

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

def mod_pow(x, n, mod):
    if n == 0: 
        return 1
    res = mod_pow(x * x % mod, n // 2, mod)
    if n % 2 == 1:
        res = res * x % mod
    return res


if is_prime(n):
    ans = False
else:
    ans = True
    for x in range(2,n):
        xpown = mod_pow(x, n, n)
        if xpown != x:
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")

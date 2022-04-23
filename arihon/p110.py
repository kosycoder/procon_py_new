n = int(input())

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

# 約数列挙
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

# 素因数分解
def prime_factor(n):
    n = int(n)
    res = {}
    i = 2
    while(1):
        if i * i > n:
            break
        while n % i == 0:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
            n /= i
            n = int(n)
        i += 1
    if n != 1:
        res[n] = 1

    return res

print(is_prime(n))
print(divisor(n))
print(prime_factor(n))

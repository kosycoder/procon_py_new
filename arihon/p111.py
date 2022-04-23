n = int(input())

# エラトステネスの篩
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

print(sieve(n))

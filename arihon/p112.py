a = int(input())
b = int(input())

is_prime = []
is_prime_small = []

def segment_sieve(a, b):    
    i = 0
    while i * i < b:
        is_prime_small.append(True)
        i += 1

    i = 0
    while i < b - a:
        is_prime.append(True)
        i += 1
    
    i = 2
    while i * i < b:
        if is_prime_small[i]:
            j = 2 * i
            while j * j < b:
                is_prime_small[j] = False
                j += i
            j = max(2, (a+i-1)// i) * i
            while j < b:
                is_prime[j-a] = False
                j += i
        i += 1

    ans = 0
    for flg in is_prime:
        if flg == True:
            ans += 1
    print(ans)

segment_sieve(a, b)

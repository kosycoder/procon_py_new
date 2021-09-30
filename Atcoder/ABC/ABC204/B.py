import sys

# from atcoder.math import convolution

MOD = 998244353

## input
# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

## type
# int()
# chr()
# ord()

## sort by lambda 
# b.append([a[itra], itra+1])
# b_sorted = sorted(b, key=lambda x:(x[0]))

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for numa in a:
        if numa<=10:
            continue
        else:
            ans += numa - 10
    
    print(ans)

if __name__ == '__main__':
    main()

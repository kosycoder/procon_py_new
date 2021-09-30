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
    n *= 108
    n = n // 100
    if n<206:
        print("Yay!")
    elif n==206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()

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
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    A = sum(a) - n//2

    if(A<=x):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

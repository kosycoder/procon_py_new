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
    x = int(input())

    if x<=39:
        print(40-x)
    elif 40<=x and x<70:
        print(70-x)
    elif 70<=x and x<90:
        print(90-x)
    else:
        print("expert")

if __name__ == '__main__':
    main()

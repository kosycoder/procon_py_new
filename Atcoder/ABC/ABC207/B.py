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
    a, b, c, d = map(int, input().split())

    if d*c<=b:
        print(-1)
    else:
        ans = a // (c*d-b)
        if (a % (c*d-b)) != 0:
            ans += 1
        print(ans)

if __name__ == '__main__':
    main()

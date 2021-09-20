import sys

# from atcoder.math import convolution

MOD = 998244353

## input
# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

## sort by lambda 
# b.append([a[itra], itra+1])
# b_sorted = sorted(b, key=lambda x:(x[0]))

def main() -> None:
    n = int(input())
    p = list(map(int, input().split()))

    s = []
    for itrn in range(n):
        s.append([p[itrn], itrn+1])
    s_sorted = sorted(s, key=lambda x:(x[0]))

    for itrn in range(n):
        if itrn != n-1:
            print(s_sorted[itrn][1], end=" ")
        else:
            print(s_sorted[itrn][1])

if __name__ == '__main__':
    main()

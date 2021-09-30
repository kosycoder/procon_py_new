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
    a_tmp = []
    for itrn in range(len(a)):
        a_tmp.append(0)

    for itrn in range(n):
        if a_tmp[a[itrn]-1] == 0:
            a_tmp[a[itrn]-1] += 1
        else:
            print("No")
            quit()
    print("Yes")

if __name__ == '__main__':
    main()

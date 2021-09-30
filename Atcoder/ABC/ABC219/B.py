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
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for itrt in range(len(t)):
        if t[itrt] == "1":
            print(s1, end="")
        if t[itrt] == "2":
            print(s2, end="")
        if t[itrt] == "3":
            print(s3, end="")

if __name__ == '__main__':
    main()

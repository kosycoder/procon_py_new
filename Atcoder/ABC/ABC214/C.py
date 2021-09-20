import sys

MOD = 998244353

def main() -> None:
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    for itrn in range(2*n):
        t[(itrn+1)%n] = min(t[(itrn+1)%n], t[itrn%n] + s[itrn%n])
    for itrt in t:
        print(itrt)

if __name__ == '__main__':
    main()

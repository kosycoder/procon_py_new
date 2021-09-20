import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    n = 0
    ans = input()
    for ians in ans:
        if ians == "A":
            n += 1
        else:
            n *= 2
    print(n)

if __name__ == '__main__':
    main()

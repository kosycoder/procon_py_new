import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    s, t = input().split()
    if s<t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

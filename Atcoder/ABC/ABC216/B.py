import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    n = int(input())

    name = []
    for itrn in range(n):
        name.append(input())
    if n == len(set(name)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()

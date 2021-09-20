import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    n = int(input())
    ans = []

    while(n!=0):
        if n%2 == 0:
            n //= 2
            ans.append("B")
        else:
            n -= 1
            ans.append("A")
    ans.reverse()
    for ians in ans:
        print(ians, end="")

if __name__ == '__main__':
    main()

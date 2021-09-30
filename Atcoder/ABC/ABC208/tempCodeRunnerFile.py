import sys

from math import factorial

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
    P = int(input())
    answer = 0
    for i in range(10, 0, -1):
        while factorial(i) <= P:
            answer += 1
            P -= factorial(i)
    print(answer)

if __name__ == '__main__':
    main()

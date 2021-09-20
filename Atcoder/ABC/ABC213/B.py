import types

import sys

MOD = 998244353

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for itra in range(len(a)):
        b.append([a[itra], itra+1])
    b_sorted = []
    b_sorted = sorted(b, key=lambda x:(x[0]))
    print(b_sorted[n-2][1])

if __name__ == '__main__':
    main()

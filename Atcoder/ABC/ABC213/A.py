import types

import sys

MOD = 998244353

def main() -> None:
    a, b = map(int, input().split())
    print(a^b)

if __name__ == '__main__':
    main()

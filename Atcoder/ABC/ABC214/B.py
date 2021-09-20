import types

import sys

MOD = 998244353

def main() -> None:
    s, t = map(int, input().split())
    ans = 0
    for a in range (101):
        for b in range (101):
            for c in range (101):
                if a+b+c<=s and a*b*c<=t:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()

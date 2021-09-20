import types

import sys

MOD = 998244353

def main() -> None:
    H, W ,N = map(int, input().split())
    x = []
    y = []
    for itrn in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    h = {ia:ix+1 for ix, ia in enumerate(sorted(set(x)))}
    w = {ib:iy+1 for iy, ib in enumerate(sorted(set(y)))}
        
    for ians in range(N):
        print(h[x[ians]], w[y[ians]])

if __name__ == '__main__':
    main()

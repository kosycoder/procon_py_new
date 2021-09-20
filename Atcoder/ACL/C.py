import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
import typing
from operator import mul
from functools import reduce
from functools import lru_cache

def floor_sum(n: int, m: int, a: int, b: int) -> int:
    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans

def solve():
    T = int(input())
    for itrt in range(T):
        n, m, a, b = map(int, input().split())
        print(floor_sum(n, m, a, b))

if __name__ == '__main__':
    solve()
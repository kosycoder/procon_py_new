import math
import typing

def DEBUG(debugoutput, flg = False):
    if flg:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

# dx, dy = [-1, -1, 1, 1], [-1, 0, -1, 0]

DEBUGFLG = False

class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))

def sieve(n):
    is_prime = [True] * (n+1)
    prime = []
    p = 0
    is_prime[0] = is_prime[1] = False
    i = 2
    for i in range(2,n+1):
        if is_prime[i]:
            p += 1
            prime.append(i)
            j = 2 * i
            while 1:
                if j > n:
                    break
                is_prime[j] = False
                j += i
    
    ans = []
    for i in range(2,n+1):
        if is_prime[i]:
            ans.append(i)

    return p, ans

A, B, P = map(int,input().split())


def solve():
    l = B - A + 1
    dsu = DSU(l)
    p, prime = sieve(l)

    for i in range(p):
        if prime[i] >= P:
            start = (A + prime[i] - 1) // prime[i] * prime[i]
            end = B // prime[i] * prime[i]

            j = start
            while(j<=end):
                dsu.merge(start-A,j-A)
                j += prime[i]

    res = 0
    for i in range(A,B+1):
        if dsu.leader(i-A) == (i-A):
            res += 1
    print(res)

solve()

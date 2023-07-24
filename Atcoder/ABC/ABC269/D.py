from collections import defaultdict

# from sys import setrecursionlimit
# setrecursionlimit(10 ** 6)

import typing


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



def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
    return l

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# MOD = 998244353

DEBUGFLG = False

N = int(input())
X = []
Y = []
for _ in range(N):
    Xtmp, Ytmp = map(int,input().split())
    X.append(Xtmp)
    Y.append(Ytmp)
DEBUG(X)
DEBUG(Y)

def convertXYintonum(x,y):
    return (x+2010)*4021+(y+2010)

dsu = DSU(4021*4021)

for i in range(N):
    for j in range(i+1,N):
        if X[i]-1 == X[j] and Y[i]-1 == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))
        if X[i]-1 == X[j] and Y[i] == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))
        if X[i] == X[j] and Y[i]-1 == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))
        if X[i] == X[j] and Y[i]+1 == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))
        if X[i]+1 == X[j] and Y[i] == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))
        if X[i]+1 == X[j] and Y[i]+1 == Y[j]:
            dsu.merge(convertXYintonum(X[i], Y[i]), convertXYintonum(X[j], Y[j]))

ans = 0   
dic = defaultdict()
for i in range(N):
    if not dsu.leader(convertXYintonum(X[i], Y[i])) in dic:
        dic[dsu.leader(convertXYintonum(X[i], Y[i]))] = 1
        ans += 1
print(ans)


DEBUG(dsu.same(convertXYintonum(0,2), convertXYintonum(1, 2)))
DEBUG(dsu.same(convertXYintonum(0,2), convertXYintonum(0, 1)))
DEBUG(dsu.same(convertXYintonum(0,2), convertXYintonum(1, 0)))
DEBUG(dsu.same(convertXYintonum(0,2), convertXYintonum(2, 0)))
DEBUG(dsu.same(convertXYintonum(0,2), convertXYintonum(-1, -1)))
DEBUG(dsu.same(convertXYintonum(1,2), convertXYintonum(0, 1)))
DEBUG(dsu.same(convertXYintonum(1,2), convertXYintonum(1, 0)))
DEBUG(dsu.same(convertXYintonum(1,2), convertXYintonum(2, 0)))
DEBUG(dsu.same(convertXYintonum(1,2), convertXYintonum(-1, -1)))
DEBUG(dsu.same(convertXYintonum(0,1), convertXYintonum(1, 0)))
DEBUG(dsu.same(convertXYintonum(0,1), convertXYintonum(2, 0)))
DEBUG(dsu.same(convertXYintonum(0,1), convertXYintonum(-1, -1)))
DEBUG(dsu.same(convertXYintonum(1,0), convertXYintonum(2, 0)))
DEBUG(dsu.same(convertXYintonum(1,0), convertXYintonum(-1, -1)))
DEBUG(dsu.same(convertXYintonum(2,0), convertXYintonum(-1, -1)))
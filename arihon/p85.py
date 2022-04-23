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

n = int(input())
k = int(input())

ds = DSU(3*n)
ans = 0
for itrk in range(k):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if x < 0 or n <= x or y < 0 or n <= y:
        ans += 1
        continue

    if t == 1:
        if (ds.same(x, y + n) or ds.same(x, y + 2*n)):
            ans += 1
        else:
            ds.merge(x, y)
            ds.merge(x + n, y + n)
            ds.merge(x + 2 * n, y + 2 * n)

    if t == 2:
        if (ds.same(x, y) or ds.same(x, y + 2 * n)):
            ans += 1
        else:
            ds.merge(x, y + n)
            ds.merge(x + n, y + 2 * n)
            ds.merge(x + 2 * n, y)
print(ans)

# 100
# 7
# 1 101 1
# 2 1 2
# 2 2 3
# 2 3 3
# 1 1 3
# 2 3 1
# 1 5 5
# 0

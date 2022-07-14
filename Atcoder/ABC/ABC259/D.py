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

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

def input_intarray():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

def judgecross(x1, y1, r1, x2, y2, r2):
    distancex2 = (x1- x2)**2 + (y1- y2)**2
    if (r1-r2)**2 <= distancex2 and distancex2 <= (r1 + r2)**2:
        return True
    else:
        return False

def judgegroupe(sx0, sy0, x0, y0, r0):
    if (sx0 - x0)**2 + (sy0 - y0)**2 == r0**2:
        return True
    else:
        return False

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N = int(input())
sx, sy, tx, ty = map(int, input().split())
x = []
y = []
r = []
for _ in range(N):
    xi, yi, ri = map(int, input().split())
    x.append(xi)
    y.append(yi)
    r.append(ri)

dsu = DSU(N)
for i in range(N):
    for j in range(i+1, N):
        # DEBUG(judgecross(x[i], y[i], r[i], x[j], y[j], r[j]))
        if judgecross(x[i], y[i], r[i], x[j], y[j], r[j]):
            dsu.merge(i, j)
if DEBUGFLG:
    for i in range(N):
        for j in range(i+1, N):
            print(i, j, dsu.same(i,j))

groups = []
groupt = []
for i in range(N):
    if judgegroupe(sx, sy, x[i], y[i], r[i]):
        groups.append(i)
    if judgegroupe(tx, ty, x[i], y[i], r[i]):
        groupt.append(i)
DEBUG(groups)
DEBUG(groupt)

ans = False
for valgroups in groups:
    for valgroupt in groupt:
        if dsu.same(valgroups, valgroupt):
            ans = True
            break

YesNo(ans)

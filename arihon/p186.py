def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

class SegmentTree:
    def __init__(self, ls: list, segfunc, identity_element):
        self.ide = identity_element
        self.func = segfunc
        self.n_origin = len(ls)
        # n以上の最小の2のべき乗
        self.num = 2 ** (self.n_origin - 1).bit_length()
        # −1はぴったりに作るためだけど気にしないでいい
        self.tree = [self.ide] * (2 * self.num - 1)
        # 木の葉に代入
        for i, l in enumerate(ls):  
            self.tree[i + self.num - 1] = l
        # 子を束ねて親を更新
        for i in range(self.num - 2, -1, -1):
            self.tree[i] = segfunc(self.tree[2 * i + 1], self.tree[2 * i + 2])

    # オリジナル要素にアクセスするためのもの
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start = idx.start if idx.start else 0
            stop = idx.stop if idx.stop else self.n_origin
            l = start + self.num - 1
            r = l + stop - start
            return self.tree[l:r:idx.step]
        elif isinstance(idx, int):
            i = idx + self.num - 1
            return self.tree[i]

    def update(self, i, x):
        # i番目の要素をxに変更する(木の中間ノードも更新する) O(logN)
        i += self.num - 1
        self.tree[i] = x
        # 木を更新
        while i:
            i = (i - 1) // 2
            self.tree[i] = self.func(self.tree[i * 2 + 1],
                                     self.tree[i * 2 + 2])

    def query(self, l, r):
        # 区間[l,r)に対するクエリをO(logN)で処理する。例えばその区間の最小値、最大値、gcdなど
        if r <= l:
            return ValueError("invalid index (l,rがありえないよ)")
        l += self.num
        r += self.num
        res_right = []
        res_left = []
        # 右から寄りながら結果を結合していくイメージ
        while l < r:
            if l & 1:
                res_left.append(self.tree[l - 1])
                l += 1
            if r & 1:
                r -= 1
                res_right.append(self.tree[r - 1])
            l >>= 1
            r >>= 1
        res = self.ide
        # 左右の順序を保って結合
        for x in res_left:
            res = self.func(x, res)
        for x in reversed(res_right):
            res = self.func(res, x)
        return res

n = int(input())
m = int(input())
s = []
t = []
for _ in range(m):
    stmp, ttmp = map(int,input().split())
    s.append(stmp)
    t.append(ttmp)

s = [ss - 1 for ss in s]
INF = 10**6
# DP配列をセグ木に乗っける(初期化済み)
dp = SegmentTree([0] + [INF] * (n - 1), min, identity_element=INF)

for ss, tt in zip(s, t):
    mi = dp.query(ss, tt)
    dp.update(tt - 1, mi + 1)

print(dp[n - 1])

# 40
# 6
# 20 30
# 1 10
# 10 20
# 20 30
# 15 25
# 30 40

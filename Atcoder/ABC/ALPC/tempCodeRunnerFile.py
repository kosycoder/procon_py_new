class Fenwick_Tree:
    def __init__(self, n, list=None):
        self.array = [0]*(n+1)
        self.n = n
        for idx, v in enumerate(list):
            self.add(idx, v)
 
    def sum_idx(self, idx):
        ret = 0
        idx += 1
        while idx > 0:
            ret += self.array[idx]
            idx -= idx & -idx
        return ret
 
    def sum_range(self, l, r):
        return self.sum_idx(r) - self.sum_idx(l-1)
 
    def add(self, idx, delta):
        idx += 1
        while idx < self.n+1:
            self.array[idx] += delta
            idx += idx & -idx

n, q = map(int, input().split())
a = list(map(int, input().split()))
f_tree = Fenwick_Tree(n=len(a), list=a)

for itrq in range(q):
    query = list(map(int, input().split()))
    if(query[0]==0):
        f_tree.add(query[1], query[2])
    else:
        print(f_tree.sum_range(query[1], query[2]-1))

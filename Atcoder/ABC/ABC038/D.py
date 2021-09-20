# WA code
class Fenwick_Tree:
    def __init__(self, num, list=None):
        self.array = [0]*(num+1)
        self.num = num

    def query(self, idx):
        ret = 0
        idx += 1
        while idx > 0:
            ret = max(ret, self.array[idx])
            idx -= idx & -idx
        return ret
 
    def update(self, idx, delta):
        idx += 1
        while idx < self.num+1:
            self.array[idx] = delta
            idx += idx & -idx

n = int(input())
box = []
for itrn in range(n):
    box.append(list(map(int, input().split())))
box.sort(key=lambda x:(x[0],-x[1]))
w = []
for itrn in range(n):
    w.append(box[itrn][1])
f_tree = Fenwick_Tree(num=100000)

dp = []
for itrn in range(n):
    dp.append(f_tree.query(w[itrn]-1)+1)
    f_tree.update(w[itrn], dp[itrn])

print(max(dp))

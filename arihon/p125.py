from copy import deepcopy

m = int(input())
p = float(input())
x = int(input())

n = 1<<m # 2^m

# 残り0ラウンド(最終ラウンド後)では
# $1M持ってるときだけ確率1，それ以外の確率は0
prv = [0]*(n+1)
prv[n] = 1

nxt = ['']*(n+1)

for r in range(m):
  # 残りr+1ラウンドのとき，所得金額区間I_iの確率を最大化
  for i in range(0, n+1):
    # 賭け金を全通り試す
    jub = min(i, n-i)
    t = 0
    for j in range(jub+1):
      t = max(t, p*prv[i+j] + (1-p)*prv[i-j])
    nxt[i] = t  # 残りr+1ラウンド・区間I_iの確率
  # prv, nxt = nxt, prv でも良い
  prv = deepcopy(nxt)  # prv = nxt は不可
  
i = x*n//1000000  # x ∈ I_i (i=0~2^m)
print(prv[i])

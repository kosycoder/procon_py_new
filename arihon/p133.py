n = int(input())
k = int(input())
wv = []
for _ in range(n):
    w, v = map(int,input().split())
    wv.append([w,v])

def flg(x):
    s = []
    for wvval in wv:
        s.append(wvval[1] - x * wvval[0])
    s = sorted(s)
    s.reverse()
    add = 0
    for ik in range(k):
        add += s[ik]
    if add >= 0:
        return True
    else:
        return False

lb = 0
rb = 1e7
while rb - lb > 0.001:
    mb = (lb + rb) / 2
    if flg(mb):
        lb = mb
    else:
        rb = mb

print(rb)

# 3
# 2
# 2 2
# 5 3
# 2 1
# --------
# 0.7502967491745949
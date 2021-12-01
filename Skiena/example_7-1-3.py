V, E, S, T = map(int, input().split()) # 頂点、辺、開始点
adj = [ [] for v in range(V)] # 隣接リスト
for e in range(E):
    s, t = map(int, input().split())
    adj[s].append(t)
    adj[t].append(s)

# 順列を格納するリスト
perm = [S]

# 順列の生成
def make_perm(n):
    if len(perm) != 0:
        if perm[len(perm)-1] == T:
            ans = []
            for itr in perm:
                ans.append(itr+1)
            print(ans)
                
    sk = adj[n]
    # print(sk)
    for x in sk:
        if x in perm:
            continue
        perm.append(x)
        # print("append ",end="")
        # print(x)
        make_perm(x)
        t = perm.pop()
        if t == S:
            perm.push(S)
        # print("pop ",end="")
        # print(t)

# print(adj)
make_perm(S)

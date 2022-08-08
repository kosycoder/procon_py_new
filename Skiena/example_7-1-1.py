n = int(input())

# 順列を格納するリスト
perm = []

# 順列の生成
def make_perm(n, perm):
    if len(perm)==n:
        itr = 0
        res = []
        for itr in range(len(perm)):
            if perm[itr] == True:
                res.append(itr+1)
        print(res)
    else:
        sk = [True, False]
        for x in sk:
            perm.append(x)
            # print("append ",end="")
            # print(x)
            make_perm(n, perm)
            t = perm.pop()
            # print("pop ",end="")
            # print(t)

make_perm(n, [])

n = int(input())

# 順列を格納するリスト
perm = []

# 順列の生成
def make_perm(n, m = 0):
    if n == m: 
        print(perm)
    else:
        m = m + 1
        sk = range(1, n + 1)
        for x in sk:
            if x in perm:
                continue
            perm.append(x)
            print("append ",end="")
            print(x)
            make_perm(n, m)
            t = perm.pop()
            print("pop ",end="")
            print(t)

make_perm(n, 0)

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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

N, M = map(int,input().split())

# 順列を格納するリスト
perm = []

# 順列の生成
def make_perm(n, m):
    if n == m:
        a = [] 
        for valperm in perm:
            a.append(valperm)
        a = sorted(a)
        if a == perm:
            print(*perm)
    else:
        m = m + 1
        sk = range(1, n + 1)
        for x in sk:
            if x in perm:
                continue
            if len(perm)!=0:
                if x <= perm[len(perm)-1]:
                    continue
            perm.append(x)
            # print("append ",end="")
            # print(x)
            make_perm(n, m)
            t = perm.pop()
            # print("pop ",end="")
            # print(t)

make_perm(M, M-N)
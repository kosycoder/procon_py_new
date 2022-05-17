from collections import defaultdict

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

W = int(input())

def div(n):
    res = []
    while n >= 1:
        res.append(n)
        n = n // 2

    return res

dic = {}
for i in range(1,W+1):
    mlist = div(i)

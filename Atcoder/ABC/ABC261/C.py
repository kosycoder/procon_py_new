from collections import defaultdict

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
N = int(input())
dic = defaultdict()

for i in range(N):
    s = input()
    if s in dic:
        print(s+"("+str(dic[s])+")")
        dic[s] += 1
    else:
        dic[s] = 1
        print(s)
    DEBUG(dic)

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

N = int(input())
A = []
Ainlist = input_intarray()
for i in range(N):
    if i != N-1:
        A.append([Ainlist[i], i+1, i + 2])
    else:
        A.append([Ainlist[i], i + 1, 1])

# print(A)

dic = {}
for i in range(N):
    dic[i+1] = 1

A = sort(A, 0, False)

ans = 0
# print(A)
for valA in A:
    print(valA)
    if (valA[1] in dic) or (valA[2] in dic):
        ans += valA[0]
        if (valA[1] in dic):
            dic.pop(valA[1])
            print(dic)
            if len(dic) == 0:
                break
        if (valA[2] in dic):
            dic.pop(valA[2])
            print(dic)
            if len(dic) == 0:
                break

print(ans)

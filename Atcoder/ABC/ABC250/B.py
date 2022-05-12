def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

N, A, B = map(int,input().split())

s1 = ""
s2 = ""

for i in range(N):
    for j in range(B):
        if i & 1:
            s1 += "#"
        else:
            s1 += "."

for vals1 in s1:
    if vals1 == ".":
        s2 += "#"
    else:
        s2 += "."

for i in range(N):
    for j in range(A):
        if i & 1:
            print(s2)
        else:
            print(s1)

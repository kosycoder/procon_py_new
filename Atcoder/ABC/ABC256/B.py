def DEBUG(debugoutput, flg = False):
    if flg:
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

ans = 0
p0 = 1
p1 = 0
p2 = 0
p3 = 0

N = int(input())
A = input_intarray()

for vala in A:
    if vala == 1:
        ans += p3
        p3 = p2
        p2 = p1
        p1 = p0

    elif vala == 2:
        ans += (p3 + p2)
        p3 = p1
        p2 = p0
        p1 = 0
    
    elif vala == 3:
        ans += (p3 + p2 + p1)
        p3 = p0
        p2 = 0
        p1 = 0

    elif vala == 4:
        ans += (p3 + p2 + p1 + 1)
        p3 = 0
        p2 = 0
        p1 = 0

print(ans)
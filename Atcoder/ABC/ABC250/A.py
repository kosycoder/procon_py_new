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

H, W = map(int,input().split())
R, C = map(int,input().split())

if H != 1 and W != 1:
    if R == H or R == 1:
        tate = 1
    else:
        tate = 2

    if C == W or C == 1:
        yoko = 1
    else:
        yoko = 2

    ans = tate + yoko

elif W == 1 and H != 1:
    if R == 1 or R == H:
        ans = 1
    else:
        ans = 2

elif H == 1 and W != 1:
    if C == 1 or C == W:
        ans = 1
    else:
        ans = 2

elif H == 1 and W == 1:
    ans = 0

print(ans)
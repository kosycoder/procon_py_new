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

A, B, C, D = map(int,input().split())
if A < C:
    print("Takahashi")
elif A > C:
    print("Aoki")
else:
    if B < D:
        print("Takahashi")
    elif B > D:
        print("Aoki")
    else:
        print("Takahashi")

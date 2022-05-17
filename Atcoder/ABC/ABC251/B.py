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

N, W = map(int,input().split())
A = input_intarray()
box = {}

ans = 0
for i1 in range(len(A)):
    box[A[i1]] = 1
    for i2 in range(i1+1, len(A)):
        box[A[i2]] = 1
        box[A[i1]+A[i2]] = 1
        for i3 in range(i2+1, len(A)):
            box[A[i3]] = 1
            box[A[i2]+A[i3]] = 1
            box[A[i3]+A[i1]] = 1
            box[A[i1]+A[i2]+A[i3]] = 1

# print(box)

for val in box:
    if val <= W:
        ans += 1

print(ans)

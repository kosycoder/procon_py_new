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
box = defaultdict(list)
for i in range(N):
    S, T = input().split()
    if S in box:
        continue
    else:
        box[S].append(int(T))
        box[S].append(i+1)

# print(box)

orgT, orgi = -1, 1000000
for valbox in box:
    # print(box[valbox])
    if box[valbox][0] > orgT or (box[valbox][0] == orgT and box[valbox][1] < orgi):
        orgT = box[valbox][0]
        orgi = box[valbox][1]

print(orgi)

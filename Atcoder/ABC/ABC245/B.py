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

N = int(input())
A = input_intarray()

arr = [False] * 2001
for valA in A:
    arr[valA] = True

for i in range(2001):
    if arr[i]:
        continue
    else:
        print(i)
        break

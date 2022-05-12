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

N, Q = map(int,input().split())

q = []
position = []
for i in range(N+1):
    q.append(i)
    position.append(i)

for i in range(Q):
    x = int(input())
    # print(x)
    # print(position[x])
    if position[x] != N:
        posl = position[x]
        q[position[x]] , q[position[x]+1] = q[position[x]+1] , q[position[x]]
        position[x] += 1
        position[q[posl]] -= 1

    else:
        posr = position[x]
        q[position[x]] , q[position[x]-1] = q[position[x]-1] , q[position[x]]
        position[x] -= 1
        position[q[posr]] += 1
    # print(q)

for i in range(len(q)):
    if i == 0:
        continue
    print(q[i],end="")
    if i != len(q)-1:
        print(" ",end="")

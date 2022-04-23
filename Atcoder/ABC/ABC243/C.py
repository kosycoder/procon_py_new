n = int(input())
xy = []
for _ in range(n):
    x, y = map(int,input().split())
    xy.append([x,y])
s = input()

xys = []
for i in range(n):
    xys.append([xy[i][0], xy[i][1], s[i]])
xys = sorted(xys, key=lambda x: x[1])
# print(xys)

nowy = xys[0][1]
ans = False
i = 0
walkR = []
walkL = []
while i <= n:
    if i < n and xys[i][1] == nowy:
        if xys[i][2] == "R":
            walkR.append(xys[i])
        else:
            walkL.append(xys[i])
    else: 
        walkR = sorted(walkR, key=lambda x: x[0])
        walkL = sorted(walkL, key=lambda x: x[0])
        # print(walkR)
        # print(walkL)
        
        if len(walkR) != 0 and len(walkL) != 0:
            if walkR[0][0] <= walkL[len(walkL)-1][0]:
                ans = True
                break
        if i != n:
            nowy = xys[i][1]
            walkR = []
            walkL = []
            if xys[i][2] == "R":
                walkR.append(xys[i])
            else:
                walkL.append(xys[i])
    i += 1

if ans == True:
    print("Yes")
else:
    print("No")

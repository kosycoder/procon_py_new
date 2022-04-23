from collections import deque

n, x = map(int,input().split())
s = input()
s = deque(s)
move = deque()

for i in range(n):
    nows = s.popleft()
    if nows == "U":
        if len(move) != 0 and (move[len(move)-1]=="L" or move[len(move)-1]=="R"):
            move.pop()
        else:
            move.append(nows)
    else:
        move.append(nows)

print(move)
for valmove in move:
    if valmove == "U":
        x = x // 2
    if valmove == "R":
        x = 2*x + 1
    if valmove == "L":
        x = 2*x
print(x)

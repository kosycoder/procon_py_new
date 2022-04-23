from collections import deque

n = int(input())
m = int(input())
maze = [list(input()) for l in range(n)]

def bfs(ntmp, mtmp):
    Q = deque()
    color = [[-1]*m for l in range(n)]
    p = [[-1]*m for l in range(n)]
    Q.append([ntmp, mtmp])
    color[ntmp][mtmp] = 0
    p[ntmp][mtmp] = 0

    while len(Q) != 0:
        Qnow = Q.popleft()
        nnow = Qnow[0]
        mnow = Qnow[1]
        if maze[nnow][mnow] == "G":
            return p[nnow][mnow]

        if nnow != 0 and (maze[nnow-1][mnow] == "." or  maze[nnow-1][mnow] == "G") and color[nnow-1][mnow] == -1:
            Q.append([nnow-1, mnow])
            color[nnow-1][mnow] = 0
            p[nnow-1][mnow] = p[nnow][mnow] + 1
        if nnow != n-1 and (maze[nnow+1][mnow] == "." or maze[nnow+1][mnow] == "G")and color[nnow+1][mnow] == -1:
            Q.append([nnow+1, mnow])
            color[nnow+1][mnow] = 0
            p[nnow+1][mnow] = p[nnow][mnow] + 1
        if mnow != 0 and (maze[nnow][mnow-1] == "." or maze[nnow][mnow-1] == "G") and color[nnow][mnow-1] == -1:
            Q.append([nnow, mnow-1])
            color[nnow][mnow-1] = 0
            p[nnow][mnow-1] = p[nnow][mnow] + 1
        if mnow != m-1 and (maze[nnow][mnow+1] == "." or maze[nnow][mnow+1] == "G") and color[nnow][mnow+1] == -1:
            Q.append([nnow, mnow+1])
            color[nnow][mnow+1] = 0
            p[nnow][mnow+1] = p[nnow][mnow] + 1
        
        color[nnow][mnow] = 1

for itrn in range(n):
    for itrm in range(m):
        if maze[itrn][itrm] == "S":
            print(bfs(itrn, itrm))
            break

# 10
# 10
# #S######.#
# ......#..#
# .#.##.##.#
# .#........
# ##.##.####
# ....#....#
# .#######.#
# ....#.....
# .####.###.
# ....#...G#
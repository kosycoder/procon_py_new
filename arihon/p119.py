n = int(input())
m = []
for _ in range(n):
    min = list(input().split())
    min = [int(i) for i in min]
    m.append(min)
a = [None] * n

def solve():
    res = 0
    for i in range(n):
        a[i] = -1
        for j in range(n):
            if m[i][j] == 1:
                a[i] = j
    
    # 上から順に確定させる
    for i in range(n):
        # i行目に来るべき行を確定させる
        # そのような行が複数あるならばすでに上にある方を優先
        pos = -1
        for j in range(i,n):
            if a[j] <= i:
                pos = j
                break
        
        # i行目に来るべき行をi行目に移動
        j = pos
        while j > i:
            a[j], a[j-1] = a[j-1], a[j]
            res += 1
            j -= 1
    
    print(res)

solve()

# 2
# 1 0   
# 1 1

# 3
# 0 0 1
# 1 0 0
# 0 1 0

# 4  
# 1 1 1 0
# 1 1 0 0 
# 1 1 0 0
# 1 0 0 0

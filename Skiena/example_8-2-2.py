INIT = 9
MATCH = 0
INSERT = 1
DELETE = 2
MAX_TYPE = 3

def calc_distance_DP(a, b):
    if a == b: return 0
    a_k = len(a)
    b_k = len(b)
    if a == "": return b_k
    if b == "": return a_k
#1---格納するための表
    matrix_cost = [[] for i in range(a_k+1)]
    matrix_parent = [[] for i in range(a_k+1)]
#2---初期化
    for i in range(a_k+1):
        matrix_cost[i] = [0 for j in range(b_k+1)]
        matrix_parent[i] = [9 for j in range(b_k+1)]
#3---0時の初期値を設定
    for i in range(a_k+1):
        matrix_cost[i][0] = i
        if i>0:
            matrix_parent[i][0] = DELETE
        else:
            matrix_parent[i][0] = INIT
    for j in range(b_k+1):
        matrix_cost[0][j] = j
        if j>0:
            matrix_parent[0][j] = INSERT
        else:
            matrix_parent[0][j] = INIT
#4---表を埋める
    for i in range(1, a_k+1):
        ac = a[i-1]
        for j in range(1, b_k+1):
            bc = b[j-1]
            opt = [9, 9, 9]
            cost = 0 if (ac == bc) else 1
            opt[MATCH] = matrix_cost[i-1][j-1] + cost
            opt[INSERT] = matrix_cost[i][j-1] + 1
            opt[DELETE] = matrix_cost[i-1][j] + 1
            matrix_cost[i][j] = opt[MATCH]
            matrix_parent[i][j] = MATCH
            for itr in range(MAX_TYPE):
                if opt[itr] < matrix_cost[i][j]:
                    matrix_cost[i][j] = opt[itr]
                    matrix_parent[i][j] = itr
    for mtrx in matrix_cost:
        print(mtrx)
    for mtrx in matrix_parent:
        print(mtrx)
    return matrix_cost[a_k][b_k]

#5---入力値
print(calc_distance_DP("thou shalt not", "you should not"))
# print(calc_distance_DP("shotagohour", "spotagogour"))

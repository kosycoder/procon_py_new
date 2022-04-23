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
# dp = [[False] * N for _ in range(2)]

N, K = map(int,input().split())
A = input_intarray()
B = input_intarray()

# dp[i][j]:i行目(A==0,B==1)のj番目の数は選ばれるか？
dp = [[False] * N for _ in range(2)]

dp[0][0] = True
dp[1][0] = True
for i in range(N-1):
    if dp[0][i] and (abs(A[i+1] - A[i]) <= K):
        dp[0][i+1] = True
    if dp[1][i] and (abs(A[i+1] - B[i]) <= K):
        dp[0][i+1] = True
    if dp[0][i] and (abs(B[i+1] - A[i]) <= K):
        dp[1][i+1] = True
    if dp[1][i] and (abs(B[i+1] - B[i]) <= K):
        dp[1][i+1] = True

YesNo(dp[0][N-1] or dp[1][N-1])

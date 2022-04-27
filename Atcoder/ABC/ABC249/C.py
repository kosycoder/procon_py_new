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

N, K = map(int, input().split())
S = []
ans = 0

for i in range(N):
    S.append(input())

for i in range(1<<N):
    Q = []
    dic = {}
    for j in range(N):
        if (i >> j) & 1:
            Q.append(S[j])
    
    for valQ in Q:
        for s in valQ:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
    for valans in range(16):
        anstmp = 0
        for valdic in dic:
            if dic[valdic] == K:
                anstmp += 1
        ans = max(ans, anstmp)

print(ans)

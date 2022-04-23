import heapq

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
A = []
MAX = int(1e6)+1
MAX2 = MAX * MAX
MAX3 = MAX2 * MAX
for i in range(MAX):
    A.append([i*i*i, i*i, i])
# print(A)

ans = int(2e18)
for valn in range(MAX):
    if A[valn][0] + A[valn][1]*MAX + A[valn][2]*MAX2 + MAX3 < N:
        continue
    if A[valn][0] > ans:
        continue
    l = 0
    r = MAX
    while l < r:
        B = (l+r)//2
        X = A[valn][0] + A[valn][1]*B + A[valn][2]*B*B + B*B*B
        if X >= N:
            ans = min(ans,X)
            r = B
        else:
            l = B + 1
    
print(ans)

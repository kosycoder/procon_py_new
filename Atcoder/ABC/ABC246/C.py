from collections import deque
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

N, K, X = map(int,input().split())
A = input_intarray()
A = sorted(A)
C = [0] * N

coupon = K
for i in range(N):
    a = A[i] // X
    C[i] = min(a, coupon)
    coupon -= C[i]
    if coupon == 0:
        break

ans = 0
if coupon == 0:
    for i in range(N):
        ans += A[i]
    ans -= K * X
else:
    for i in range(N):
        A[i] -= C[i] * X
    A = sorted(A, reverse=True)
    for i in range(N):
        if i < coupon:
            continue
        ans += A[i]
        
print(ans)

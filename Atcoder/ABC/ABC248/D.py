import bisect

def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

N = int(input())
arr = [[] for i in range(200001)]
A = input().split()
A = [int(i) for i in A]
for i in range(N):
    arr[A[i]].append(i)
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    print(bisect.bisect_left(arr[X], R) - bisect.bisect_left(arr[X], L-1))

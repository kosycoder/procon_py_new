from collections import deque

def SelectionSort(a):
    res = []
    n = len(a)
    for i in range(n):
        minimum = a.popleft()
        for j in range(len(a)):
            nownum = a.popleft()
            a.append(max(nownum, minimum))
            minimum = min(nownum, minimum)
        res.append(minimum)
    print(res)

datanum = int(input())
dq = deque()
for i in range(datanum):
    dq.append(int(input()))

SelectionSort(dq)

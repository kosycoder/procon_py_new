import bisect

def DEBUG(debugoutput):
    if DEBUGFLG:
        print(debugoutput)

def sort(l, num = 0, revflg = False):
    l = sorted(l, key=lambda x: x[num], reverse=revflg)
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

DEBUGFLG = False

X, A, D, N = map(int,input().split())

ans1 = abs(A-X)
DEBUG(ans1)

ans2 = abs(A+D*(N-1)-X)
DEBUG(ans2)

ans3 = ans2
if D!=0:
    n = (X-A)//D
    for i in range(n-5, n+6, 1):
        ndash = min(max(i, 1),N)
        ans3 = min(ans3, abs(A+D*(ndash-1)-X))
        DEBUG(ans3)

ans = min(ans1, ans2, ans3)
print(ans)

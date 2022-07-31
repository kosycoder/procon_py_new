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

N = int(input())
a = input().split()
a = [int(i) for i in a]

b = [int(i+1) for i in range(N)]

arev = a[::-1]
brev = b[::-1]
S = [-1]
for i in range(N):
    if arev[i] == brev[i]:
        S.append(S[i]+1)
    else:
        S.append(S[i])
S = S[::-1]
DEBUG(a)
DEBUG(b)

ans1 = 0
ans2 = 0
for i in range(N):
    if a[i] == b[i]:
        ans1 += S[i]
    else:
        if i+1 == a[a[i]-1]:
            ans2 += 1

ans = ans1 + ans2//2
print(ans)

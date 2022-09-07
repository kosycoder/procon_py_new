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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# MOD = 998244353

DEBUGFLG = False
S = input()
S = [str(i) for i in S]
for i in range(len(S)):
    if S[i] =="a":
        S[i] = str(0)
    if S[i] =="t":
        S[i] = str(1)
    if S[i] =="c":
        S[i] = str(2)
    if S[i] =="o":
        S[i] = str(3)
    if S[i] =="d":
        S[i] = str(4)
    if S[i] =="e":
        S[i] = str(5)
    if S[i] =="r":
        S[i] = str(6)
S = [int(i) for i in S]
# print(S)

ans = 0
for i in range(len(S)):
    j = i
    while j > 0 :
        if S[j] < S[j-1]:
            S[j], S[j-1] = S[j-1], S[j]
            ans += 1
        j -= 1
print(ans)

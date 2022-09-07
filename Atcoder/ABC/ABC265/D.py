from logging.handlers import WatchedFileHandler


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
MAX = int(1e6)

N, P, Q, R = map(int,input().split())
A = input().split()
A = [int(i) for i in A]

Stmp = [0]
for i in range(len(A)):
    Stmp.append(Stmp[i]+A[i])

S = {}
for valS in Stmp:
    if valS in S:
        S[valS] += 1
    else:
        S[valS] = 1

for valS in S:
    if valS+P in S and valS+P+Q in S and valS+P+Q+R in S:
        print("Yes")
        exit()

print("No")



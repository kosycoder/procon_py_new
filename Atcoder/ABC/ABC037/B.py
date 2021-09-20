N, Q = map(int, input().split())
L = []
R = []
T = []

for itrq in range(Q):
    Lin, Rin, Tin = map(int, input().split())
    L.append(Lin)
    R.append(Rin)
    T.append(Tin)

ans = []
for itrn in range(N):
    ans.append(0)

for itrq in range(Q):
    for itrn in range(N):
        if(itrn+1<L[itrq] or R[itrq]<=itrn):
            continue
        else:
            ans[itrn] = T[itrq]

for itr in range(len(ans)):
    print(ans[itr])

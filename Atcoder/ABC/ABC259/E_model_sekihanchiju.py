from collections import defaultdict
n=int(input())
D=defaultdict(list)
A=[[] for _ in range(n)]
for i in range(n):
  m=int(input())
  for j in range(m):
    p,e=map(int,input().split())
    A[i].append([p,e])
    D[p].append(e)
    D[p].sort()
    if len(D[p])==3:
      D[p].pop(0)
ans=0
#print(A)
#print(D)
for i in range(n):
  flag=False
  for j in range(len(A[i])):
    p,e=A[i][j][0],A[i][j][1]
    if len(D[p])==1:
      flag=True
      break
    if D[p][1]==e and D[p][0]<D[p][1]:
      flag=True
      break
  if flag:
    ans+=1
print(min(ans+1,n))


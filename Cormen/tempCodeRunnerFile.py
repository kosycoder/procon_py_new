MAXINT = int(1e9)

n = int(input())
p = list(map(int,input().split()))
m =  [[-1]*(n+1) for l in range(n+1)]
s =  [[-1]*(n+1) for l in range(n+1)]

def printparens(i,j):
    if i == j:
        print("A",end="")
        print(i, end="")
    else:
        print("(", end="")
        printparens(i,s[i][j])
        printparens(s[i][j]+1,j)
        print(")", end="")

for itr in range(1,n+1):
    m[itr][itr] = 0

for l in range(2,n+1):
    for i in range(1,n-l+2):
        j = i + l - 1
        m[i][j] = MAXINT
        for k in range(i,j):
            q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
print(m[1][6])
printparens(1,6)

ans = []
def solve():
    n, k = map(int,input().split())
    sf = input()
    sr = sf[::-1]
    count = 0
    for itr in range((n+1)//2):
        if sf[itr] != sr[itr]:
            count += 1
    ans.append(abs(k-count))

def disp(itmp):
    print("Case #",end="")
    print(itmp+1,end="")
    print(": ",end="")
    print(ans[itmp])

t = int(input())
for itr in range(t):
    solve()
for itr in range(t):
    disp(itr)

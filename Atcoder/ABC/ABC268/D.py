from collections import defaultdict
import itertools

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

DEBUGFLG = True

N, M = map(int,input().split())
S = []
for _ in range(N):
    Sin = input()
    S.append(Sin)

T = defaultdict()
for _ in range(M):
    Tin = input()
    T[Tin] = 1

def dfs(word, cur, remain):
    if remain < 0:
        return
    
    if cur == N:
        if word.size() >= 3 and not(word in T):
            print(word)
            exit()
        return
    
    if len(word) > 0 and word[len(word)-1] != "_":
        dfs(word+"_", cur, remain)
    else:
        dfs(word+S[cur], cur+1, remain)
        if word.size() > 0:
            dfs(word+"_", cur, remain-1)

dfs("", 0, 16)

print(-1)   

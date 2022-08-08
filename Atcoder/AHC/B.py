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

def calc_score(X):
    score = 0
    last = [-1] * SIZE
    for day in range(D):
        type = X[day]
        score += s[day][type]
        last[type] = day
        score -= sum(c[j] * (day - last[j]) for j in range(SIZE))
        print(score) ##########
    return score

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

SIZE = 26

D = int(input())
c = [*map(int, input().split())]
s = [[*map(int, input().split())] for _ in range(D)]

tvec = []
for valD in range(D):
    tin = int(input()) - 1
    tvec.append(tin)
calc_score(tvec)

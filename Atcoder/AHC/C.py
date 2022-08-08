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
    return score

def prev_day(X, day, type):
    for i in range(day - 1, -1, -1):
        if X[i] == type:
            return i
    return -1

def next_day(X, day, type):
    for i in range(day + 1, D):
        if X[i] == type:
            return i
    return D

def calc_scorediff(X, day, type):
    diff = 0

    # delete X[day]
    diff -= s[day][X[day]]
    prv, nxt = prev_day(X, day, X[day]), next_day(X, day, X[day])
    diff += c[X[day]] * (prv - day) * (nxt - day)

    # insert type
    diff += s[day][type]
    prv, nxt = prev_day(X, day, type), next_day(X, day, type)
    diff += c[type] * (day - prv) * (nxt - day)

    return diff

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

SIZE = 26

D = int(input())
c = [*map(int, input().split())]
s = [[*map(int, input().split())] for _ in range(D)]

t = []
for valD in range(D):
    tin = int(input()) - 1
    t.append(tin)

M = int(input())
dq = [[*map(int, input().split())] for _ in range(M)]

score = calc_score(t)
for m in range(M):
    scorediff = calc_scorediff(t, dq[m][0]-1, dq[m][1]-1)
    t[dq[m][0]-1] = dq[m][1]-1
    score += scorediff
    print(score)

from math import log
from random import randint, random
from time import time

SIZE = 26


def prev_day(X, day, type):
    for i in range(day - 1, -1, -1):
        if X[i] == type:
            return i
    return -1


def next_day(X, day, type):
    for i in range(day + 1, d):
        if X[i] == type:
            return i
    return d


def calc_score(X):
    score = 0
    last = [-1] * SIZE
    for day in range(d):
        type = X[day]
        score += S[day][type]
        last[type] = day
        score -= sum(C[j] * (day - last[j]) for j in range(SIZE))
    return score


def calc_score_diff(X, day, type):
    """
    Y = X[:]
    Y[day] = type
    return calc_score(Y) - calc_score(X)
    """
    diff = 0

    # delete X[day]
    diff -= S[day][X[day]]
    prv, nxt = prev_day(X, day, X[day]), next_day(X, day, X[day])
    diff += C[X[day]] * (prv - day) * (nxt - day)

    # insert type
    diff += S[day][type]
    prv, nxt = prev_day(X, day, type), next_day(X, day, type)
    diff += C[type] * (day - prv) * (nxt - day)
    return diff


def greedy_method():
    X = []
    last = [-1] * SIZE
    for day in range(d):
        cand = []
        for type in range(SIZE):
            cand.append([0, type])
            cand[-1][0] += S[day][type]
            cand[-1][0] -= sum(C[j] * (day - last[j]) for j in range(SIZE) if j != type)
        type = max(cand)[1]
        last[type] = day
        X.append(type)
    return X


def random_method():
    return [randint(0, SIZE - 1) for _ in range(d)]


def hill_climbing_method(X0, duration):
    time0 = time()
    X = X0[:]
    score = calc_score(X)
    cntloop = 0
    while time() - time0 < duration:
        if randint(0, 1):
            # 1 点更新
            day, type = randint(0, d - 1), randint(0, SIZE - 1)
            new_score = score + calc_score_diff(X, day, type)
            stash = X[day]
            X[day] = type
            if new_score > score:
                score = new_score
            else:
                X[day] = stash
        else:
            # 2 点 swap
            day0 = randint(0, d - 2)
            day1 = randint(day0 + 1, min(day0 + 16, d - 1))
            stash0, stash1 = X[day0], X[day1]
            new_score = score
            new_score += calc_score_diff(X, day0, stash1)
            X[day0] = stash1
            new_score += calc_score_diff(X, day1, stash0)
            X[day1] = stash0
            if new_score > score:
                score = new_score
            else:
                X[day0], X[day1] = stash0, stash1
        cntloop += 1
    print(cntloop)
    print(score)
    return X


def simulated_annealing_method(X, duration):
    time0 = time()
    X = X0[:]
    score = calc_score(X)
    while time() - time0 < duration:
        if randint(0, 1):
            # 1 点更新
            day, type = randint(0, d - 1), randint(0, SIZE - 1)
            new_score = score + calc_score_diff(X, day, type)
            stash = X[day]
            X[day] = type
            # if new_score > score or random() < pow(1.003, new_score - score):
            if new_score - score > log(random(), 1.003):
                score = new_score
            else:
                X[day] = stash
        else:
            # 2 点 swap
            day0 = randint(0, d - 2)
            day1 = randint(day0 + 1, min(day0 + 16, d - 1))
            stash0, stash1 = X[day0], X[day1]
            new_score = score
            new_score += calc_score_diff(X, day0, stash1)
            X[day0] = stash1
            new_score += calc_score_diff(X, day1, stash0)
            X[day1] = stash0
            # if new_score > score or random() < pow(1.003, new_score - score):
            if new_score - score > log(random(), 1.003):
                score = new_score
            else:
                X[day0], X[day1] = stash0, stash1
    print(score)
    return X


if __name__ == "__main__":
    d = int(input())
    C = [*map(int, input().split())]
    S = [[*map(int, input().split())] for _ in range(d)]
    X0 = greedy_method()
    X1 = hill_climbing_method(X0, duration=1.8)
    #X1 = simulated_annealing_method(X0, duration=1.8)
    print(*[type + 1 for type in X1], sep="\n")
    # print(calc_score(X1))

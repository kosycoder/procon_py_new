g = 10.0

n = int(input())
h = int(input())
r = int(input())
T = int(input())

def calc(T):
    if T < 0:
        return h
    t = pow(2*h/g,0.5)
    k = T // t
    if k % 2 == 0:
        d = T - k * t
        return h - g * d * d / 2
    else:
        d = k * t + t - T
        return h - g * d * d / 2

def solve():
    y = [0] * n
    for i in range(n):
        y[i] = calc(T-i)
    y = sorted(y)
    for i in range(n):
        print(y[i]+2*r*i/100.0)

solve()
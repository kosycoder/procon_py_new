def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

A, B, C, D, E, F, X = map(int,input().split())

t = B * (X // (A + C)) * A
t += B * min(X % (A + C), A)
a = E * (X // (D + F)) * D
a += E * min(X % (D + F), D)

if t > a:
    print("Takahashi")
elif t < a:
    print("Aoki")
else:
    print("Draw")

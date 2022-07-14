def DEBUG(debugoutput, flg = False):
    if flg:
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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

A = input_intarray()

h1 = A[0]
h2 = A[1]
h3 = A[2]
w1 = A[3]
w2 = A[4]
w3 = A[5]

ans = 0
for d in range(1,29):
    for g in range(1,29):
        if w1 - d - g < 1:
            continue
        for b in range(1,29):
            for h in range(1,29):
                if w2 - b - h < 1:
                    continue
                for c in range(1,29):
                    for f in range(1,29):
                        if w3 - c - f < 1:
                            continue
                        if h1 == b + c + w1 - d - g:
                            if h2 == d + f + w2 - b - h :
                                if h3 == g + h - c - f + w3:
                                    ans += 1
                                    # print(w1 - d - g,b,c,d,w2 - b - h,f,g,h,w3 - c - f)
print(ans)

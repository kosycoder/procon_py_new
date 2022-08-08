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

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

DEBUGFLG = False

A, B, C, D, E = map(int,input().split())
arr = [A, B, C, D, E]
arr = sorted(arr)

flg = False
if arr[0] == arr[1] == arr[2] and arr[2] != arr[3] and arr[3] == arr[4]:
    flg = True
if arr[0] == arr[1] and arr[1] != arr[2] and arr[2] == arr[3] == arr[4]:
    flg = True
    
YesNo(flg)
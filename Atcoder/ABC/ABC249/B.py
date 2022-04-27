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

S = input()

flg1 = False
for i in range(len(S)):
    if ord('A') <= ord(S[i]) <= ord('Z'):
        flg1 = True

flg2 = False
for i in range(len(S)):
    if ord('a') <= ord(S[i]) <= ord('z'):
        flg2 = True

flg3 = True
S = sorted(S)
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        flg3 = False
        break

YesNo(flg1 and flg2 and flg3)

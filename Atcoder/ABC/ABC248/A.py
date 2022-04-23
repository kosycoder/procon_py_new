def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

s = input()
l = [False] * 10
for vals in s:
    l[int(vals)] = True

i = 0
while 1:
    if l[i]:
        i += 1
        continue
    else:
        print(i)
        break

n = int(input())

box = [True] * (2*n+2)

while 1:
    i = 1
    while i <= 2*n+2:
        if box[i] == True:
            print(i)
            box[i] = False
            i += 1
            break
        else:
            i += 1
            continue
    
    aoki = int(input())
    if aoki == 0:
        break
    else:
        box[aoki] = False

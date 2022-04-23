k = int(input())

s = str(format(k, 'b'))
for itrs in s:
    if itrs == '0':
        print("0",end="")
    else:
        print("2",end="")
print()

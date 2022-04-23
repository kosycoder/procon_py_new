a, b, c, x = map(int,input().split())

if a >= x:
    print(1.0)
elif x > b:
    print(0.0)
else:
    print(c/(b-a))


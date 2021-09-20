hw = [list(map(int, input().split())) for i in range(2)]

if (hw[0][0]==hw[1][0] or hw[0][0]==hw[1][1]\
    or hw[0][1]==hw[1][0] or hw[0][1]==hw[1][1]):
        print("YES")
else:
     print("NO")
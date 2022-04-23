s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

ans = False
if s1 == t1 and s2 == t2 and s3 == t3:
    ans = True
if s1 == t2 and s2 == t3 and s3 == t1:
    ans = True
if s1 == t3 and s2 == t1 and s3 == t2:
    ans = True

YesNo(ans)

def sort(l, num, flg):
    l = sorted(l, key=lambda x: x[num], reverse=flg)
    return l

def YesNo(flg):
    if flg == True:
        print("Yes")
    else:
        print("No")

a, b, k = map(int,input().split())

ans = 0
while a < b:
    a *= k
    ans += 1

print(ans)

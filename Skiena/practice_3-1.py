s = input()

a = []

def func():
    count = 0
    for itr in s:
        count += 1
        if itr == "(":
            a.append("(")
        else:
            if bool(a) == False:
                print("No")
                return count
            else:
                ch = a.pop()
                if ch == "(":
                    pass
                else:
                    a.append(")")
                    a.append(")")
    if bool(a) == False:
        print("Yes")
        return 0
    else:
        print("No")
        return count

if __name__ == '__main__':
    res = func()
    if(res):
        print(res)

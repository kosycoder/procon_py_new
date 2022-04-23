n = int(input())
s = []
for i in range(n):
    s.append(input())

def solve():
    for i in range(n):
        for j in range(n):
            # 上に一列
            if 0<=j-5:
                count = 0
                for l in range(6):
                    if s[i][j-l] == ".":
                        count += 1
                if count<=2:
                        return True
            # 下に一列
            if j+5<n:
                count = 0
                for l in range(6):
                    if s[i][j+l] == ".":
                        count += 1
                if count<=2:
                        return True
            # 右に一列
            if i+5<n:
                count = 0
                for l in range(6):
                    if s[i+l][j] == ".":
                        count += 1
                if count<=2:
                        return True
            # 左に一列
            if 0<=i-5:
                count = 0
                for l in range(6):
                    if s[i-l][j] == ".":
                        count += 1
                if count<=2:
                        return True
            # 右下がり
            if i+5<n and j+5<n:
                count = 0
                for l in range(6):
                    if s[i+l][j+l] == ".":
                        count += 1
                if count<=2:
                        return True
            # 左下がり
            if i+5<n and 0<=j-5:
                count = 0
                for l in range(6):
                    if s[i+l][j-l] == ".":
                        count += 1
                if count<=2:
                        return True
            # 右上がり
            if 0<=i-5 and j+5<n:
                count = 0
                for l in range(6):
                    if s[i-l][j+l] == ".":
                        count += 1
                if count<=2:
                        return True
            # 左上がり
            if 0<=i-5 and 0<=j-5:
                count = 0
                for l in range(6):
                    if s[i-l][j-l] == ".":
                        count += 1
                if count<=2:
                        return True
    return False

if solve():
    print("Yes")
else:
    print("No")

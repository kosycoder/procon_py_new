import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    s = input()
    for itrn in range(len(s)):
        if s[itrn] == ".":
            y = int(s[itrn+1])
            if itrn == 2:
                x = 10*int(s[itrn-2])+int(s[itrn-1])
            else:
                x = int(s[itrn-1])
    
    if y<=2:
        print(x, end="")
        print("-")
    elif 3<=y and y<=6:
        print(x)
    else:
        print(x, end="")
        print("+")

if __name__ == '__main__':
    main()

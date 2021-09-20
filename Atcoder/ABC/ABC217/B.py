import sys

MOD = 998244353

# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

def main() -> None:
    b = False
    r = False
    g = False
    h = False

    for itrn in range(3):
        s = input()
        if s == "ABC":
            b = True
        if s == "ARC":
            r = True
        if s == "AGC":
            g = True
        if s == "AHC":
            h = True
        
    if b == False:
        print("ABC")
    if r == False:
        print("ARC")
    if g == False:
        print("AGC")
    if h == False:
        print("AHC")

if __name__ == '__main__':
    main()

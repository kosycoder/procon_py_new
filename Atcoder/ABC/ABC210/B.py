import sys

# from atcoder.math import convolution

MOD = 998244353

## input
# n = int(input())
# n1, n2 = map(int, input().split())
# s = list(map(int, input().split()))
# s, k = input().split()
# k = int(k)

## type
# int()
# chr()
# ord()

## sort by lambda 
# b.append([a[itra], itra+1])
# b_sorted = sorted(b, key=lambda x:(x[0]))

def main() -> None:
    n = int(input())
    s = input()
    
    cnt = 0
    while(1-int(s[cnt])):
        cnt += 1

    if cnt%2 == 0:
        print("Takahashi")
    else:
        print("Aoki")
    
if __name__ == '__main__':
    main()
